from test_parse_html import href_to_shortcode
from test_parse_html import get_hrefs_srcs
from test_parse_html import src_to_img_id
import psycopg2 as pg2
import random
import os

def insert_tracker(shortcode, username, id):
	"""
	Add a row into table 'tracker' for new image
	"""
	q = " INSERT INTO tracker (shortcode, username, img_id) values ( '{}', '{}', '{}');"
	return q.format(shortcode, username, id)

def insert_softmax(shortcode, vector):
	"""
	Add a row into table 'softmax' for new image
	"""
	q = '''INSERT INTO softmax (shortcode, softmax) values ('{}', '{}');'''
	return q.format(shortcode, vector)

def insert_fc8(shortcode, vector):
	"""
	Add a row into table 'fc8' for new image
	"""
	q = '''INSERT INTO fc8 (shortcode, fc8) values ('{}', '{}');'''
	return q.format(shortcode, vector)

def insert_fc7(shortcode, vector):
	"""
	Add a row into table 'fc7' for new image
	"""
	q = '''INSERT INTO fc7 (shortcode, fc7) values ('{}', '{}');'''
	return q.format(shortcode, vector)


def create_tracker():
	"""
	Populate table 'tracker' with information from each image from each user from each group
	"""
	# flag to help with debugging
	DEBUG = False
	# seven categories of user profiles. 'raw' will be called 'most_popular' later in pipeline
	USER_GROUPS = ['raw', 'foodies', 'photographers', 'travel', 'models', 'dogs', 'cats']

	for group in USER_GROUPS:
		# get a list of profile directories for a given user group; directory contains images
		dirs = [dir for dir in os.listdir('../data/{}/'.format(group)) if dir.endswith('.html') and not dir.startswith('._')]
		# print out directories to see where problem is happening
		if DEBUG:
			dirs = dirs[:5]
	            print 'dirs: {}'.format(dirs)
	    # go through each file
		while len(dirs) > 0:
			fname = dirs.pop()
			# extract href and source information from file
			hrefs, srcs = get_hrefs_srcs(fname, group)
			# move on to next file once we've exhausted hrefs and sources
			if len(hrefs) == 0 or len(srcs) == 0: continue
			# find out the shortcode and username information
			shortcodes, username = href_to_shortcode(hrefs)
			# convert source information to usable ids
			ids = src_to_img_id(srcs)
			# status update to terminal for given user
			print 'user: {}'.format(username)
			# edgecase when page was improperly loaded/saved
			if len(shortcodes) != len(ids):
				print 'user {} len(shortcodes): {}, len(ids): {}'.format(username, len(shortcodes), len(ids))
				continue
			# randomize images to eliminate time structure of page & images
			pairs = zip(shortcodes, ids) 
			random.shuffle(pairs)
			# check whether user is already in table
			c.execute('''SELECT COUNT(*) FROM tracker WHERE username = '{}';'''.format(username))
			user_count = int(c.fetchall()[0][0])

			if user_count == 0:
				# insert new rows into table 'tracker'
				print 'inserting for user {}'.format(username)
				for (code, img_id) in pairs:
					c.execute( insert_tracker(code, username, img_id) )
				conn.commit()
			else:
				print '{} already has {} entries in tracker'.format(username, user_count)
	conn.commit()
	conn.close()


if __name__ == '__main__':
	'''
		        Table "public.tracker"
	  Column   |  Type   |    Modifiers
	-----------+---------+-----------------
	 shortcode | text    | not null
	 username  | text    |
	 img_id    | text    |
	 predicted | integer | default 0
	Indexes:
	    "tracker_pkey" PRIMARY KEY, btree (shortcode)
	'''

	conn = pg2.connect(dbname='image_clusters', host='/var/run/postgresql/')
	c = conn.cursor()

	create_tracker()
	
