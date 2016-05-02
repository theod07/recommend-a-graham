import numpy as np
import pandas as pd
import psycopg2 as pg2
import os
import random
import shutil
from pg_to_df import CATEGORIES

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
	return usernames

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

def copy_imgs_to_dir(category, dirmap):
	with open('../data/{}_imgs_to_show.csv'.format(category), 'r') as f:
		lines = f.readlines()
		lines = [l for l in lines if not l.startswith('username')]
	for line in lines:
		user, img_id = line.split(', ')
		img_id = img_id.split('\n')[0]
		try:
			shutil.copy2('../data/{}/{}/{}'.format(cat, dirmap[user], img_id), 
						'../imgs/{}/{}_{}'.format(category, user, img_id))
		except:
			print 'error {}, {}'.format(user, img_id)


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