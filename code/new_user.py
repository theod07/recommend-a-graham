import os
import numpy as np
from operator import xor
import matplotlib.pyplot as plt
from skimage.io import imshow
import psycopg2 as pg2
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


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


def new_user_mean_vector(imgs, conn, vtype='softmax'):
	# extract img_id from imgs
	parsed = map(lambda x: x.split('_'), imgs)
	img_ids = map(lambda x: '_'.join(x[-4:]), parsed)

	# create query to extract shortcodes
	q1 = '''
		SELECT username, 
				shortcode, 
				predicted
		FROM tracker
		WHERE img_id IN ('{}');
		'''.format("','".join(img_ids))
	df1 = pd.read_sql(q1, conn)

	shortcodes_csv = "','".join(df1.shortcode.values)
	q2 = '''
		SELECT {0}
		FROM {0}
		where shortcode IN ('{1}');
		'''.format(vtype, shortcodes_csv)
	df2 = pd.read_sql(q2, conn)
	df2[vtype] = df2[vtype].apply(lambda x: np.fromstring(x[1:-1], sep='\n'))

	mean_vector = np.mean(df2[vtype].values)

	return mean_vector


if __name__ == '__main__':

	CATEGORIES = ['cats', 'dogs']
	
	try:
		conn = pg2.connect(dbname='image_clusters')
	except:
		conn = pg2.connect(dbname='image_clusters', host='/var/run/postgresql/')
	
	# choose the vector type you want to inspect
	for vtype in ['fc7', 'fc8', 'softmax']:
		# pick imgs to show new_user
		imgs = random_pick_imgs(CATEGORIES)

		# likes = show_user_imgs(imgs)
		# simulate getting new_user's preference
		like_idx = np.array([[1]*10, [0]*10]).astype('bool').reshape(20)
		liked_photos = imgs[like_idx]

		mean_vector = new_user_mean_vector(liked_photos, conn, vtype)
		mean_arr = np.load('../data/{}_arr.npy'.format(vtype))

		cosine_sims = cosine_similarity(mean_arr, mean_vector)
		users = pd.read_sql('''SELECT DISTINCT username FROM tracker;''', conn).values

		top20 = np.argsort(cosine_sims, axis=0)[-20:]
		most_sim = users[top20]
		print 'categories: {}, prefs: {}'.format(CATEGORIES, like_idx)
		print 'most_sim_users : {}'.format(users[top20].flatten())

