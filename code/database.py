import os
import psycopg2 as pg2
from test_parse_html import get_hrefs_srcs
from test_parse_html import href_to_shortcode
from test_parse_html import src_to_img_id
import random

def insert_tracker(shortcode, username, id):
	q = " INSERT INTO tracker (shortcode, username, img_id) values ( '{}', '{}', '{}');"
	return q.format(shortcode, username, id)

def insert_softmax(shortcode, vector):
	q = '''INSERT INTO softmax (shortcode, softmax) values ('{}', '{}');'''
	return q.format(shortcode, vector)

def insert_fc8(shortcode, vector):
	q = '''INSERT INTO fc8 (shortcode, fc8) values ('{}', '{}');'''
	return q.format(shortcode, vector)

def insert_fc7(shortcode, vector):
	q = '''INSERT INTO fc7 (shortcode, fc7) values ('{}', '{}');'''
	return q.format(shortcode, vector)


def create_tracker():
	DEBUG = False
	USER_GROUPS = ['raw', 'foodies', 'photographers', 'travel', 'models']

	# dirs = [dir for dir in os.listdir('../data/raw/')+os.listdir('../data/travel/')+os.listdir('../data/foodies/') if dir.endswith('.html')]


	for group in USER_GROUPS:
		dirs = [dir for dir in os.listdir('../data/{}/'.format(group)) if dir.endswith('.html') and not dir.startswith('._')]

		if DEBUG:
			dirs = dirs[:5]
	            	print 'dirs: {}'.format(dirs)

		while len(dirs) > 0:
			fname = dirs.pop()
			hrefs, srcs = get_hrefs_srcs(fname, group)
			print 'len(hrefs): {}, len(srcs): {}'. format(len(hrefs), len(srcs))


			if len(hrefs) == 0 or len(srcs) == 0:
				print 'len(hrefs): {}, len(srcs): {}'. format(len(hrefs), len(srcs))
				continue
			
			shortcodes, username = href_to_shortcode(hrefs)
			ids = src_to_img_id(srcs)
			print 'user: {}'.format(username)

			if len(shortcodes) != len(ids):
				print 'user {} len(shortcodes): {}, len(ids): {}'.format(username, len(shortcodes), len(ids))
				continue

			pairs = zip(shortcodes, ids) 
			random.shuffle(pairs)

			# check whether user is already in table
			c.execute('''SELECT COUNT(*) FROM tracker WHERE username = '{}';'''.format(username))
			user_count = int(c.fetchall()[0][0])

			if user_count == 0:
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

	# create_tracker()
	
