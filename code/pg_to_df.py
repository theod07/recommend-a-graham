from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from tempfile import TemporaryFile
import matplotlib.pyplot as plt
import psycopg2 as pg2
import pandas as pd
import numpy as np
import os
plt.style.use('ggplot')

# CATEGORIES = ['most_popular','photographers', 'travel', 'foodies', 'models', 'cats', 'dogs'] 
CATEGORIES = ['cats', 'dogs']

def get_mean_vectors(user, conn, vec_name='softmax'):
	"""
	INPUT: username for instagram,
			connection object to postgres database

	OUTPUT: user's mean vector, taken from table vec_name
	"""
	
	query1 = '''SELECT shortcode FROM tracker WHERE username = '{}';'''.format(user)
	df = pd.read_sql(query1, conn)
	# strip brackets from string
	shortcode_list = map(lambda x: "'"+str(x)+"'", df['shortcode'].values.flatten())
	shortcodes_csv = ','.join(shortcode_list)
	# create query string
	query2 = '''SELECT {0} FROM {0} WHERE shortcode IN ({1});'''.format(vec_name, shortcodes_csv)
	df = pd.read_sql(query2, conn)

	df[vec_name] = df[vec_name].apply(lambda x: np.fromstring(x[1:-1], sep='\n'))

	vector_arr = df[vec_name].values

	return np.mean(vector_arr)
	
def get_users_arr(conn, vtype):
	"""
	INPUT: connection object to postgres database
			vtype: either 'softmax', 'fc8', 'fc7'
	OUTPUT: numpy array of users' mean vectors.
			row-by-colum :: user-by-features
	"""

	mean_vectors = []
	df = pd.read_sql('''SELECT DISTINCT username FROM tracker;''', conn)

	users = []
	for user in df['username']:
		try:
			mean_vector = get_mean_vectors(user, conn, vec_name=vtype)
			mean_vectors.append(mean_vector[np.newaxis, :])
			users.append(user)
		except IndexError:
			print 'invalid index for {}'.format(user)
	mean_arr = np.concatenate(mean_vectors, axis=0)
	
	return mean_arr, users

def get_pca_models(mean_arr):
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
		plt.savefig('../figures/pca_{}_components.jpg'.format(n_comps))

		plt.figure()
		plt.plot(pca.explained_variance_ratio_, linewidth=2)
		plt.axis('tight')
		plt.xlabel('n_components')
		plt.ylabel('explained_variance_ratio_')
		plt.title('Principal Component Analysis on Users')
		plt.savefig('../figures/pca_ratio_{}_components.jpg'.format(n_comps))

		plt.figure()
		plt.plot(np.cumsum(pca.explained_variance_ratio_), linewidth=2)
		plt.axis('tight')
		plt.xlabel('n_components')
		plt.ylabel('cumsum_variance_ratio_')
		plt.title('PCA on Users, cumsum(explained_variance_ratio_)')
		plt.savefig('../figures/pca_cumsum_{}_components.jpg'.format(n_comps))

		plt.close('all')

	return pca_models



if __name__ == '__main__': 
	username = 'marshanskiy' # 'paolatonight', 'ashleyrparker', 'eyemediaa', 'parisinfourmonths'
	
	try:
		conn = pg2.connect(dbname='image_clusters')
	except:
		conn = pg2.connect(dbname='image_clusters', host='/var/run/postgresql/')

	# choose the vector type you want to inspect
	vtype = 'fc7'
	# calculate mean softmax vector for all users
	# store vectors in matrix
	if '{}_arr.npy'.format(vtype) in os.listdir('../data/'):
		mean_arr = np.load('../data/{}_arr.npy'.format(vtype))
	else:
		mean_arr, users = get_users_arr(conn, vtype)
		np.save('../data/{}_arr'.format(vtype), mean_arr)

	# standardize features by removing mean and scaling to unit variance
	scaler = StandardScaler()
	mean_arr_scaled = scaler.fit_transform(mean_arr)
	
	# create a pca_model for different values of explained variance
	# pca_models = get_pca_models(sm_arr_scaled)







	
