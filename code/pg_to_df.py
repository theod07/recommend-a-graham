import psycopg2 as pg2
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import os
from tempfile import TemporaryFile
from sklearn.preprocessing import StandardScaler
plt.style.use('ggplot')

# CATEGORIES = ['photographers', 'travel', 'foodies', 'models', 'cats', 'dogs'] # excluding 'most_popular' because useless
CATEGORIES = ['cats', 'dogs']

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


def shortcodes_from_tracker(username, conn):
	
	return username, df.shortcode.values

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
	
def get_sm_arr(conn):
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

def get_pca_models(sm_arr):
	"""
	INPUT: scaled 2D array of softmax vectors

	OUTPUT: list of pca models of various amount of variance explained
			save plots of explained variance in ../data/ directory
	"""

	pca_models = []
	for n_comps in [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, None]:
		# create pca model that will retain 70% explained variance
		pca = PCA(n_components=n_comps)
		pca_models.append(pca)
		# fit model on mean softmax vectors
		# transform softmax vectors to reduced feature space
		sm_pca = pca.fit_transform(sm_arr_scaled)
		plt.figure()
		plt.plot(pca.explained_variance_, linewidth=2)
		plt.axis('tight')
		plt.xlabel('n_components')
		plt.ylabel('explained_variance_')
		plt.title('Principal Component Analysis on Users')
		plt.savefig('../data/pca_{}_components.jpg'.format(n_comps))

		plt.figure()
		plt.plot(pca.explained_variance_ratio_, linewidth=2)
		plt.axis('tight')
		plt.xlabel('n_components')
		plt.ylabel('explained_variance_ratio_')
		plt.title('Principal Component Analysis on Users')
		plt.savefig('../data/pca_ratio_{}_components.jpg'.format(n_comps))

		plt.figure()
		plt.plot(np.cumsum(pca.explained_variance_ratio_), linewidth=2)
		plt.axis('tight')
		plt.xlabel('n_components')
		plt.ylabel('cumsum_variance_ratio_')
		plt.title('PCA on Users, cumsum(explained_variance_ratio_)')
		plt.savefig('../data/pca_cumsum_{}_components.jpg'.format(n_comps))

		plt.close('all')

	return pca_models

def random_pick_imgs():
	imgs = []
	for cat in CATEGORIES:
		df = pd.read_csv('../data/{}_imgs_to_show.csv'.format(cat), sep=', ', engine='python')

		choices = np.random.choice(xrange(df.shape[0]), size=10, replace=False)
		for z in zip(df.username[choices], df.img_id[choices]):
			imgs.append(z)
	return imgs

if __name__ == '__main__': 
	username = 'marshanskiy' # 'paolatonight', 'ashleyrparker', 'eyemediaa', 'parisinfourmonths'
	
	try:
		conn = pg2.connect(dbname='image_clusters')
	except:
		conn = pg2.connect(dbname='image_clusters', host='/var/run/postgresql/')

	# calculate mean softmax vector for all users
	# store vectors in matrix
	if not 'sm_arr.npy' in os.listdir('../data/'):
		sm_arr = get_sm_arr(conn)
		np.save('../data/sm_arr', sm_arr)
	else:
		sm_arr = np.load('../data/sm_arr.npy')

	# standardize features by removing mean and scaling to unit variance
	scaler = StandardScaler()
	sm_arr_scaled = scaler.fit_transform(sm_arr)
	
	pca_models = get_pca_models(sm_arr_scaled)

	select_imgs = random_pick_imgs()





	
