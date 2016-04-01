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
			WHERE username='{}' AND predicted=0
			LIMIT 5;'''
	return q.format(username)

def update_predicted(shorts_imgs):
	q = '''UPDATE tracker AS t 
			SET predicted=1 
			FROM (values {:}) AS done(shortcode, img_id) 
			WHERE done.shortcode=t.shortcode;'''
	return q.format(', '.join(map(str, shorts_imgs)))
	
def get_dirmap():
	with open('../data/html_map.txt', 'r') as f:
		lines = f.read().splitlines()
	dirs = {}
	for line in lines:
		kv = line.split('!@#$!@#$!@#$ ')
		dirs[kv[0]] = kv[1]
	return dirs

if __name__ == '__main__':
	
	DEBUG = False
	USER_GROUP = raw_input('enter user_group:')

	with open('../data/{}.txt'.format(USER_GROUP), 'r') as f:
		lines = f.readlines()
		lines = [l for l in lines if not l.startswith('#')]
		usernames = [l.split('\n')[0] for l in lines]

	if DEBUG:
		usernames = usernames[:2]
	else:
		usernames = usernames

	# load the mapping from username to directoryname
	dirmap = get_dirmap()

	# connect to postgres
	try:
		conn = pg2.connect(dbname='image_clusters')
	except:
		conn = pg2.connect(dbname='image_clusters', host='/var/run/postgresql/')

	c = conn.cursor()
	nnet = vgg16()
	
	# c.execute(insert_softmax(conn, 'aaaaa', np.random.rand(1000)))
	# c.execute(insert_fc8(conn, 'aaaaa', np.random.rand(4096)))
	# c.execute(insert_fc7(conn, 'aaaaa', np.random.rand(4096)))

	# conn.commit()

	for i in range(5000):	
		for username in usernames:
			c.execute(get_shorts_imgs(username))
			shorts_imgs = c.fetchall()
			print 'shorts_imgs: {}'.format(shorts_imgs)

			if len(shorts_imgs) == 0:
				continue
			for short, img in shorts_imgs:
				try:
					softmax, fc8, fc7 = nnet.predict('../data/{}/{}/{}'.format(USER_GROUP, dirmap[username], img))
					print 'softmax.shape {}'.format(softmax.shape)
					c.execute(insert_softmax(short, softmax))
					c.execute(insert_fc8(short, fc8))
					c.execute(insert_fc7(short, fc7))
				except:				
					with open('../logs/log_predict_to_pg.txt', 'ab') as f:
						f.write('fail predicting for {} {} {}\n'.format(USER_GROUP, username, img))

			c.execute(update_predicted(shorts_imgs))
			conn.commit() #need execute in order to update db