import psycopg2 as pg2
import pandas as pd
import numpy as np


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

def get_user_softmax_mean(user, conn):
	"""
	INPUT: username for instagram,
			connection object to postgres database

	OUTPUT: user's mean softmax vector
	"""
	query1 = '''SELECT shortcode FROM tracker WHERE username = '{}';'''.format(user)
	df = pd.read_sql(query1, conn)
	# strip brackets from string
	shortcode_list = map(lambda x: "'"+str(x)+"'", df['shortcode'].values.flatten())
	shortcodes_csv = ','.join(shortcode_list)
	# create query string
	query2 = '''SELECT softmax FROM softmax WHERE shortcode IN ({});'''.format(shortcodes_csv)
	df = pd.read_sql(query2, conn)

	df.softmax = df.softmax.apply(lambda x: np.fromstring(x[1:-1], sep='\n'))

	soft_arr = df.softmax.values

	return np.mean(soft_arr)
	
def get_sm_matrix(conn):
	sm_mean_vectors = []
	df = pd.read_sql('''SELECT DISTINCT username FROM tracker;''', conn)

	for user in df['username']:
		try:
			softmax_mean_vector = get_user_softmax_mean(user, conn)
			sm_mean_vectors.append(softmax_mean_vector[np.newaxis, :])
		except IndexError:
			print 'invalid index for {}'.format(user)
	sm_matrix = np.concatenate(sm_mean_vectors, axis=0)
	
	return sm_matrix

if __name__ == '__main__': 
	username = 'marshanskiy' # 'paolatonight', 'ashleyrparker', 'eyemediaa', 'parisinfourmonths'
	
	try:
		conn = pg2.connect(dbname='image_clusters')
	except:
		conn = pg2.connect(dbname='image_clusters', host='/var/run/postgresql/')

	sm_matrix = get_sm_matrix(conn)



	
