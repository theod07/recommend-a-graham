import psycopg2 as pg2
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
plt.style.use('ggplot')

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
	"""
	INPUT: connection object to postgres database

	OUTPUT: numpy array of users' mean softmax vectors.
			row-by-colum :: user-by-softmax
	"""

	sm_mean_vectors = []
	df = pd.read_sql('''SELECT DISTINCT username FROM tracker;''', conn)

	for user in df['username']:
		try:
			softmax_mean_vector = get_user_softmax_mean(user, conn)
			sm_mean_vectors.append(softmax_mean_vector[np.newaxis, :])
		except IndexError:
			print 'invalid index for {}'.format(user)
	sm_arr = np.concatenate(sm_mean_vectors, axis=0)
	
	return sm_arr

if __name__ == '__main__': 
	username = 'marshanskiy' # 'paolatonight', 'ashleyrparker', 'eyemediaa', 'parisinfourmonths'
	
	try:
		conn = pg2.connect(dbname='image_clusters')
	except:
		conn = pg2.connect(dbname='image_clusters', host='/var/run/postgresql/')

	# calculate mean softmax vector for all users
	# store vectors in matrix
	sm_arr = get_sm_matrix(conn)
	
	for n_comps in [None, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
		# create pca model that will retain 70% explained variance
		pca = PCA(n_components=0.7)
		# fit model on mean softmax vectors
		# transform softmax vectors to reduced feature space
		sm_pca = pca.fit_transform(sm_arr)
		plt.figure()
		plt.plot(pca.explained_variance_, linewidth=2)
		plt.axis('tight')
		plt.xlabel('n_components')
		plt.ylabel('explained_variance_')
		plt.title('Principal Component Analysis on Users')
		plt.savefig('../data/pca_{}_components.jpg'.format(n_comps))




	
