import numpy as np
import pandas as pd
import psycopg2 as pg2
import os
import random
import shutil
from pg_to_df import CATEGORIES
from tfidf_fc8 import make_user_category_dict

# HTMLS_DIR = '~/Volumes/panther/recommend-a-graham/data'

def get_dirmap():
	with open('../data/html_map.txt', 'r') as f:
		lines = f.read().splitlines()
	dirs = {}
	for line in lines:
		kv = line.split('!@#$!@#$!@#$ ')
		dirs[kv[0]] = kv[1]
	return dirs

def get_usernames(category):
	with open('../data/{}.txt'.format(category), 'r') as f:
		lines = f.readlines()
		lines = [l for l in lines if not l.startswith('#')]
		usernames = [l.split('\n')[0] for l in lines]
	return username

def imgs_to_show(CATEGORIES):

	dirmap = get_dirmap()

	for category in CATEGORIES:
		usernames = get_usernames(category)

		for username in usernames:
			try:
				files = os.listdir('../data/{}/{}'.format(category,dirmap[username]))
				jpgs = [f for f in files if f.endswith('.jpg')]

				if len(jpgs) < 10:
					selected = jpgs
				else:
					selected = np.random.choice(jpgs, size=10, replace=False)

				with open('../data/{}_imgs_to_show.csv'.format(category), 'a') as f:
					for jpg in selected:
						print jpg
						f.write('{}, {}\n'.format(username, jpg))
			except KeyError:
				continue
			except OSError:
				continue

def sample_predicted_imgs(category, conn):
	'''
	Generate a list of imgs that have already been predicted for each category.
	These lists will be used to draw random sample of imgs from to present to new user

	INPUT: category
			connection object to postgres database
	OUTPUT: None. (write to file)
	'''

	usernames = get_usernames(category)

	q = '''
		SELECT shortcode,
				username,
				img_id
		FROM tracker
		WHERE username
		IN ('{}')
		AND predicted = 1;
		'''.format("','".join(usernames))

	df = pd.read_sql(q, conn)

	for username in df.username.unique():
		user_df = df[df.username==username]
		if user_df.shape[0] < 10:
			sample = user_df.index
		else:
			sample = np.random.choice(user_df.index, size=10, replace=False)

		with open('../data/{}_imgs_to_show.csv'.format(category), 'a') as f:
			for i in sample:
				f.write('{}, {}\n'.format(df.ix[i]['username'],df.ix[i]['img_id']))

def copy_imgs_to_dir(dirmap):
	"""
	open fc8_pkl_<username>.pkl file
	extract shortcodes
	extract img_id for first 100imgs for user
	copy each img_id from html dir to ./imgs/<user>
	"""
	dirs = os.listdir('../fc8_pkls/')
	user_pkls = [dir for dir in dirs if dir.startswith('fc8_')]
	tracker_df = pd.read_pickle('./tracker.pkl')
	user_cat_dict = make_user_category_dict()

	for fname in user_pkls:
		print fname
		user = fname.split('fc8_')[-1].split('.pkl')[0]
		df = pd.read_pickle('../fc8_pkls/{}'.format(fname))
		if df.shape[0] < 100:
			shortcodes = df.shortcode.values
		else:
			shortcodes = df.shortcode.values[:100]
		# shortcodes_csv = "','".join(shortcodes)
		img_ids = tracker_df[tracker_df.shortcode.apply(lambda x: x in shortcodes)]['img_id']
		category = user_cat_dict[user]

		if not user in os.listdir('../imgs/{}/'.format(category)):
			os.mkdir('../imgs/{}/{}'.format(category, user))

		for img_id in img_ids:
			shutil.copy2('../data/{}/{}/{}'.format(category, dirmap[user], img_id),
							'../imgs/{}/{}/{}'.format(category, user, img_id))



if __name__ == '__main__':
	try:
		conn = pg2.connect(dbname='image_clusters')
	except:
		conn = pg2.connect(dbname='image_clusters', host='/var/run/postgresql/')

	# imgs_to_show(CATEGORIES)

	dirmap = get_dirmap()

	for cat in CATEGORIES:
	# make a file of imgs to choose from (already predicted)
	# 	sample_predicted_imgs(cat, conn)
		copy_imgs_to_dir(cat, dirmap)
