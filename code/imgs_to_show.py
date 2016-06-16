from tfidf_fc8 import make_user_category_dict
from pg_to_df import CATEGORIES
import psycopg2 as pg2
import pandas as pd
import numpy as np
import random
import shutil
import os

def get_dirmap():
	"""
	load dictionary
	{username: directoryname}
	"""
	# read file
	with open('../data/html_map.txt', 'r') as f:
		lines = f.read().splitlines()
	dirs = {}
	for line in lines:
		# split on custom delimiter
		kv = line.split('!@#$!@#$!@#$ ')
		# update dictionary
		dirs[kv[0]] = kv[1]
	return dirs

def get_usernames(category):
	"""
	get list of usernames for a given category
	"""
	# read in file
	with open('../data/{}.txt'.format(category), 'r') as f:
		lines = f.readlines()
		# filter out irrelevant lines
		lines = [l for l in lines if not l.startswith('#')]
		# strip \n characters
		usernames = [l.split('\n')[0] for l in lines]
	return username

def imgs_to_show(CATEGORIES):
	"""
	show images
	"""
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
	will allow us to access a sample of images more quickly
	"""
	# generate list of pkl files
	dirs = os.listdir('../fc8_pkls/')
	# filter out any irrelevant files
	user_pkls = [dir for dir in dirs if dir.startswith('fc8_')]
	# load tracker_df from saved file
	tracker_df = pd.read_pickle('./tracker.pkl')
	# load dictionary of user categories
	user_cat_dict = make_user_category_dict()
	# iterate through pkl files
	for fname in user_pkls:
		# print status to terminal
		print fname

		user = fname.split('fc8_')[-1].split('.pkl')[0]
		# create dataframe from file
		df = pd.read_pickle('../fc8_pkls/{}'.format(fname))
		# choose a subset of a user's images to transfer
		if df.shape[0] < 100:
			# select all images if user has fewer than 100
			shortcodes = df.shortcode.values
		else:
			# select first 100 images if user has more than 100
			shortcodes = df.shortcode.values[:100]
		# determine the corresponding img_ids
		img_ids = tracker_df[tracker_df.shortcode.apply(lambda x: x in shortcodes)]['img_id']
		category = user_cat_dict[user]
		# create directory for user if it's not there already
		if not user in os.listdir('../imgs/{}/'.format(category)):
			os.mkdir('../imgs/{}/{}'.format(category, user))
		# copy the selected images to new directory for easy access
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
