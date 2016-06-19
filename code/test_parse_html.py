from time import strftime as strftime
from bs4 import BeautifulSoup
import pandas as pd
import os

def get_hrefs_srcs(fname, user_group):
	"""
	take in a html file and return the hrefs and img_src 
	links associated with user's page

	INPUT:  fname, string filename
			user_group, string name of group that user belongs to
	OUTPUT: hrefs, list containing href tags
			srcs, list of 
	"""
	# Load html file into beautifulsoup
	with open('../data/{}/{}'.format(user_group, fname), 'r') as f:
		soup = BeautifulSoup(f, 'lxml')

	a_tags = soup('a')
	hrefs, srcs = [], []
	for tag in a_tags:
		if tag('img'):
			hrefs.append(tag['href'])
			srcs.append(tag('img')[0]['src'])
	return hrefs, srcs

def href_to_shortcode(hrefs):
	"""
	extract shortcodes and username from href tags
	shortcode is a unique string that identifies an image

	INPUT:  hrefs, list of href tags
	OUTPUT: shortcodes, list of unique codes that identifies images
			username, string 
	"""
	shortcodes = []
	for href in hrefs:
		left = href.split('/?taken-by=')[0]
		shortcodes.append(left.split('instagram.com/p/')[-1])
	username = hrefs[-1].split('/?taken-by=')[-1]
	return shortcodes, username

def src_to_img_id(srcs):
	"""
	extract img_ids from source links

	INPUT:  srcs, list of source links from a user's raw page
	OUTPUT: img_ids, list of image filenames
	"""
	img_ids = []
	for src in srcs:
		img_ids.append(src.split('/')[-1])
	return img_ids

def save_df(username, shortcodes, img_ids):
	"""
	store a user's content information in a pandas dataframe.
	save the dataframe to file
	
	INPUT:  username, string 
			shortcodes, list of shortcode strings
			img_ids, list of image name strings
	OUTPUT: None, pandas dataframe saved to local disk
	"""
	if len(shortcodes) != len(img_ids): 
		print '{} Fail. len(shortcodes) != len(img_ids) for user: {}'.format(strftime('%Y%m%d.%H:%M:%s'), username)
		return
	df = pd.DataFrame(columns=['shortcode', 'img_id'])
	df.shortcode = shortcodes
	df.img_id = img_ids
	df.to_pickle('../data/pickles/{}.pkl'.format(username))
	print '{} saved to pickles/{}.pkl'.format(strftime('%Y%m%d.%H:%M:%s'), username)



if __name__ == '__main__':

	USER_GROUP = 'raw'

	dirs = [dir for dir in os.listdir('../data/{}/'.format(USER_GROUP)) if dir.endswith('.html')]

	while len(dirs) > 0:
		fname = dirs.pop()
		hrefs, srcs = get_hrefs_srcs(fname, USER_GROUP)

		if len(hrefs) == 0 or len(srcs) == 0:
			print 'len(hrefs): {}, len(srcs): {}'. format(len(hrefs), len(srcs))
			continue
		
		shortcodes, username = href_to_shortcode(hrefs)
		img_ids = src_to_img_id(srcs)

		if '{}.pkl'.format(username) in os.listdir('../data/pickles/'):
			print '{} already have a pickle for {}'.format(strftime('%Y%m%d.%H:%M:%s'), username)
		else:
			save_df(username, shortcodes, img_ids)
