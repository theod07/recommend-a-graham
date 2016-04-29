import psycopg2 as pg2
import pandas as pd

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

def get_user_shortcodes(user, conn):
	query = '''SELECT shortcode FROM tracker WHERE username = '{}';'''.format(user)
	shortcodes = pd.read_sql(query, conn)
	return shortcodes

softmaxs = []
df = pd.read_sql('''SELECT DISTINCT USERNAME FROM TRACKER;''', conn)

for user in df['username']:
