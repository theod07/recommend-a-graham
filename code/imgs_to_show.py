import numpy as np
import os
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

def imgs_to_show(CATEGORIES):
	
	dirmap = get_dirmap()

	for category in CATEGORIES:
		with open('../data/{}.txt'.format(category), 'r') as f:
			lines = f.readlines()
			lines = [l for l in lines if not l.startswith('#')]
			users = [l.split('\n')[0] for l in lines]

		for user in users:
			try:
				files = os.listdir('../data/{}/{}'.format(category,dirmap[user]))
				jpgs = [f for f in files if f.endswith('.jpg')]
				selected = np.random.choice(jpgs, size=10, replace=False)

				with open('../data/imgs_to_show.csv', 'a') as f:
					for jpg in selected:
						print jpg
						f.write('{}, {}\n'.format(user, jpg))
			except KeyError:
				continue
			except OSError:
				continue
if __name__ == '__main__':
	imgs_to_show(CATEGORIES)