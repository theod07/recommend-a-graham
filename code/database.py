import os
import psycopg2 as pg2
from test_parse_html import get_hrefs_srcs
from test_parse_html import href_to_shortcode
from test_parse_html import src_to_img_id
import random

def insert(shortcode, username, id):
	q = " INSERT INTO tracker (shortcode, username, img_id) values ( '{}', '{}', '{}');"
	return q.format(shortcode, username, id)



if __name__ == '__main__':
	'''
		        Table "public.tracker"
	  Column   |  Type   |    Modifiers
	-----------+---------+-----------------
	 shortcode | text    | not null
	 username  | text    |
	 img_id    | text    |
	 predicted | boolean | default bool(0)
	Indexes:
	    "tracker_pkey" PRIMARY KEY, btree (shortcode)
	'''

	conn = pg2.connect(dbname='image_clusters')
	c = conn.cursor()

	DEBUG = True


	dirs = [dir for dir in os.listdir('../data/raw/')+os.listdir('../data/travel/')+os.listdir('../data/foodies/') if dir.endswith('.html')]

	if DEBUG:
		dirs = dirs[:2]

	while len(dirs) > 0:
		fname = dirs.pop()
		hrefs, srcs = get_hrefs_srcs(fname)

		if len(hrefs) == 0 or len(srcs) == 0:
			print 'len(hrefs): {}, len(srcs): {}'. format(len(hrefs), len(srcs))
			continue
		
		shortcodes, username = href_to_shortcode(hrefs)
		ids = src_to_img_id(srcs)

		if len(shortcodes) != len(ids):
			print 'user {} len(shortcodes): {}, len(ids): {}'.format(username, len(shortcodes), len(ids))
			continue

		pairs = zip(shortcodes, ids) 
		random.shuffle(pairs)

		# check whether user is already in table
		c.execute('''SELECT COUNT(*) FROM tracker WHERE username = '{}';'''.format(username))

		user_count = int(c.fetchall()[0][0])
				
		print '{} already has {} entries in tracker'.format(username, user_count)

		if user_count == 0:
			for (code, img_id) in pairs:
				c.execute( insert(code, username, img_id) )
			conn.commit()

	conn.commit()
	conn.close()