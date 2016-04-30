import psycopg2 as pg2
import pandas as pd
import numpy as np

try:
	conn = pg2.connect(dbname='image_clusters')
except:
	conn = pg2.connect(dbname='image_clusters', host='/var/run/postgresql/')

# USER_GROUPS = ['photographers', 'travel', 'most_popular', 'foodies', 'models', 'cats', 'dogs']
# 
# for group in USER_GROUPS:
# 	print 'retrieving data for {}'.format(group)
# 	with open('../data/{}.txt'.format(group), 'r') as f:
# 		lines = f.readlines()
# 		lines = [l for l in lines if not l.startswith('#')]
# 		usernames = [l.split('\n')[0] for l in lines]
# 	df = psql.frame_query(\
# 		'''SELECT * FROM fc7 WHERE username IN ({});'''\
# 		.format("'"+"', '".join(usernames)+"'"), conn)
# 
# 	df.to_pickle('./{}.pkl'.format(group))

def get_user_shortcodes_csv(user, conn):
	query1 = '''SELECT shortcode FROM tracker WHERE username = '{}';'''.format(user)
	df = pd.read_sql(query1, conn)
	# Strip bracket
	shortcode_list = map(lambda x: "'"+str(x)+"'", df['shortcode'].values.flatten())
	shortcodes_csv = ','.join(shortcode_list)
	
	query2 = '''SELECT softmax FROM softmax WHERE shortcode IN ({});'''.format(shortcodes_csv)
	softmaxs_df = pd.read_sql(query2, conn)

	return softmaxs_df
	


softmaxs = []
df = pd.read_sql('''SELECT DISTINCT USERNAME FROM TRACKER;''', conn)

# for user in df['username']:
# 	shortcodes_csv = get_user_shortcodes(user, conn)
# 	q = '({})'.format(shortcodes_csv)

if __name__ == '__main__': 
	username = 'marshanskiy'
	print get_user_shortcodes_csv(username, conn)
