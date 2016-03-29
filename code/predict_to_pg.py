import os
import cPickle as pickle
import psycopg2 as pg2
from database import insert_softmax, insert_fc8, insert_fc7
import numpy as np
from vgg16_cpu import vgg16
np.set_printoptions(threshold=np.nan)

def get_shorts_imgs(username):
	q = '''SELECT shortcode, img_id 
			FROM tracker 
			WHERE username='{}' 
			LIMIT 100;'''
	return q.format(username)

def update_predicted(shorts_imgs):
	q = '''UPDATE tracker AS t 
			SET predicted=1 
			FROM (values {:}) AS done(shortcode, img_id) 
			WHERE done.shortcode=t.shortcode;'''
	return q.format(', '.join(map(str, shorts_imgs)))
	
conn = pg2.connect(dbname='image_clusters')
c = conn.cursor()


usernames = ['taylorswift']
for username in usernames:
	c.execute(get_shorts_imgs(username))
	shorts_imgs = c.fetchall()
	print 'shorts_imgs: {}'.format(shorts_imgs)

	# for short, img in shorts_imgs:
	# 	softmax, fc8, fc7 = predict(img)
	# 	insert_softmax(short, softmax)
	# 	insert_fc8(short, fc8)
	# 	insert_fc7(short, fc7)

	# c.execute(update_predicted(shorts_imgs))
	# conn.commit() #need execute in order to update db

if __name__ == '__main__':
	imgs = [ f for f in os.listdir('.') if f.endswith('.jpg')]
	nnet = vgg16()
	for img in imgs:
		softmax, fc8, fc7 = nnet.predict(img, local_img='True')

		print 'softmax.shape: {}'.format(softmax.shape)
		print 'fc8.shape: {}'.format(fc8.shape)
		print 'fc7.shape: {}'.format(fc7.shape) 