from sklearn.metrics.pairwise import cosine_similarity
from html_map import user_group_dictionary
import matplotlib.pyplot as plt
from skimage.io import imshow
from operator import xor
import psycopg2 as pg2
import pandas as pd
import numpy as np
import os


def show_user_imgs(imgs):
	'''
	Display images to new_user and prompt for response (Like / NoLike)
	Keep track of preferences in a list.
	
	INPUT: list of pairs, (username, img_id)

	OUTPUT: np.array of new_user's preferences (zero or one)
	'''
	# initialize the list of preferences
	likes = []
	for img in imgs:
		# generate the path to the image
		fname = '../imgs/{}'.format(img)
		# update status to terminal
		print fname
		# show image to user
		imshow(fname)
		plt.show()
		# initialize string of preferences
		pref = ''
		# logical xor in python is != ... i know, right??
		while not pref in ['0', '1']:
			# survey whether user liked photo
			print 'you entered: {}'.format(pref)
			pref = raw_input('Did you like that photo? Yes:1, No:0...')
			# keep track of the result in list 'likes'
			likes.append(int(pref))
	# convert list 'likes' to np.array for better handling downstream
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
		# random subset selection
		choices = np.random.choice(os.listdir('../imgs/{}'.format(cat)), size=10, replace=False)
		for choice in choices:
			# add it to the list!
			imgs.append('{}/{}'.format(cat,choice))
	# convert list 'imgs' to np.array for better handling downstream
	imgs = np.array(imgs)
	return imgs


def new_user_mean_vector(imgs, conn, vtype='softmax'):
	"""
	calculate new_user's preference vector as the mean of their vectors
	INPUT: 		imgs, list of names of images
				conn, connection object to postgres database
				vtype, string name of neuralnetwork output vector; also the name of table in postgres database

	OUTPUT: 	numpy vector representing a user's preference
	"""
	# extract img_id from imgs
	parsed = map(lambda x: x.split('_'), imgs)
	img_ids = map(lambda x: '_'.join(x[-4:]), parsed)
	# create query to extract from table 'tracker'
	q1 = '''
		SELECT username, 
				shortcode, 
				predicted
		FROM tracker
		WHERE img_id IN ('{}');
		'''.format("','".join(img_ids))
	# save query results as dataframe
	df1 = pd.read_sql(q1, conn)
	# join individual shortcodes as a comma separated string for SQL to understand
	shortcodes_csv = "','".join(df1.shortcode.values)
	q2 = '''
		SELECT {0}
		FROM {0}
		WHERE shortcode IN ('{1}');
		'''.format(vtype, shortcodes_csv)
	# save new query results as a dataframe
	df2 = pd.read_sql(q2, conn)
	# convert vector results from string format to np.array
	df2[vtype] = df2[vtype].apply(lambda x: np.fromstring(x[1:-1], sep='\n'))
	# treat a user's preference as the mean of their images
	mean_vector = np.mean(df2[vtype].values)
	return mean_vector


def main(vtype='fc7'):
	"""
	display images to user
	collect new_users preference for each image
	represent new_user's preference as a mean of their vectors
	determine the user from our list most similar to new_user's preference

	INPUT: 		vtype, string name of the vector to do calculations
	OUTPUT: 	None
	"""
	CATEGORIES = ['cats', 'dogs']
	try:
		conn = pg2.connect(dbname='image_clusters')
	except:
		conn = pg2.connect(dbname='image_clusters', host='/var/run/postgresql/')
	# pick imgs to show new_user
	imgs = random_pick_imgs(CATEGORIES)
	# likes = show_user_imgs(imgs)
	# simulate getting new_user's preference temporarily
	like_idx = np.array([[1]*10, [0]*10]).astype('bool').reshape(20)
	# filter images new_user prefers
	liked_photos = imgs[like_idx]
	# calculate preference vector
	mean_vector = new_user_mean_vector(liked_photos, conn, vtype)
	# load all users mean vectors as np.array from file
	mean_arr = np.load('../data/{}_arr.npy'.format(vtype))
	# cosine similarity metric for closeness
	cosine_sims = cosine_similarity(mean_arr, mean_vector)
	# get the usernames
	users = pd.read_sql('''SELECT DISTINCT username FROM tracker;''', conn).values
	# determine the users most similar to new_user
	top_users = np.argsort(cosine_sims, axis=0)[-6:-1:1]
	most_sim = users[top_users].flatten()
	print 'categories: {}, vtype: {}'.format(CATEGORIES, vtype)
	print 'most_sim_users : {}'.format(users[top_users].flatten())
	# print out results of most similar users along with their user_group
	for sim in most_sim:
		for k,v in user_group_dictionary.items():
			if sim in v:
				print 'group: {}  user: {} '.format(k,sim)


if __name__ == '__main__':

	vtype = 'fc7'
	main(vtype)
	