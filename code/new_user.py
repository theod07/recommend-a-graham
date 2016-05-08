import os
import numpy as np
from operator import xor
import matplotlib.pyplot as plt
from skimage.io import imshow
import psycopg2 as pg2


def show_user_imgs(imgs):
	'''
	Display images to new_user and prompt for response (Like/NoLike)
	Keep track of preferences in a list.
	
	INPUT: list of pairs, (username, img_id)

	OUTPUT: list of new_user's preferences (zero or one)
	'''
	likes = []
	for img in imgs:
		fname = '../imgs/{}'.format(img)
		print fname
		# imshow(fname)
		imshow(fname)
		plt.show()

		pref = ''
		# logical xor in python is != ... i know, right??
		while not pref in ['0', '1']:
			print 'you entered: {}'.format(pref)
			pref = raw_input('Did you like that photo? Yes:1, No:0...')
			likes.append(int(pref))
	likes = np.array(likes).astype('bool')
	return likes


def random_pick_imgs(categories):
	'''
	Randomly select 10 imgs from each category to be shown to new user.
	INPUT: None
	
	OUTPUT: list of lists of images.
	'''
	imgs = []
	for cat in categories:
		choices = np.random.choice(os.listdir('../imgs/{}'.format(cat)), size=10, replace=False)
		for choice in choices:
			imgs.append('{}/{}'.format(cat,choice))
	imgs = np.array(imgs)
	return imgs


def new_user_softmax_mean(imgs, conn):
	# extract img_id from imgs
	parsed = map(lambda x: x.split('_'), imgs)
	img_ids = map(lambda x: '_'.join(x[-4:]), parsed)

	q1 = '''
		SELECT username, 
				shortcode, 
				predicted
		FROM tracker
		WHERE img_id IN ('{}');
		'''.format("','".join(imgs))
	
	df = pd.read_sql(q1, conn)
	return df


if __name__ == '__main__':

	CATEGORIES = ['cats', 'dogs']
	
	try:
		conn = pg2.connect(dbname='image_clusters')
	except:
		conn = pg2.connect(dbname='image_clusters', host='/var/run/postgresql/')
	
	imgs = random_pick_imgs(CATEGORIES)
	print imgs
	# likes = show_user_imgs(imgs)

	# simulate getting new_user's preference
	like_idx = np.array([[1]*10, [0]*10]).astype('bool').reshape(20)
	liked_photos = imgs[like_idx]

	df = new_user_softmax_mean(liked_photos, conn)

	# user_short_pred_df = new_user_softmax_mean(imgs, conn)