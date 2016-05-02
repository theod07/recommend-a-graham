import numpy as np
import os
import random
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
	usernamess = get_usernames(category)

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
		sample = np.random.choice(user_df.index, size=10, replace=False)
		with open('../data/{}_imgs_to_show.csv', 'a') as f:
			for i in sample:
				f.write('{}, {}, {}\n'.format(df.ix[i][['username','img_id']]))


if __name__ == '__main__':
	try:
		conn = pg2.connect(dbname='image_clusters')
	except:
		conn = pg2.connect(dbname='image_clusters', host='/var/run/postgresql/')

	# imgs_to_show(CATEGORIES)

	for cat in CATEGORIES:
		sample_predicted_imgs(cat, conn)
