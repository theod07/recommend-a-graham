import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import psycopg2 as pg2
conn = pg2.connect(dbname='image_clusters', host='/var/run/postgresql/')


sample_users = ['goemon16', 'andrew_icant', 'instagramtop50', 'lebackpacker']
# tracker_df = pd.read_pickle('./tracker.pkl')

def explore1():
	shortcodes = [] # len4 list of len100 lists of shortcodes
	for user in sample_users:
		user_df = tracker_df[tracker_df.username == user]
		user_df = user_df[user_df.predicted == 1]
		shorts = np.random.choice(user_df.shortcode.values, size=100, replace=False)
		shortcodes.append(shorts)

	shortcodes_csv = map(lambda x: "','".join(x), shortcodes)

	users_vectors = []
	for i, user in enumerate(sample_users):
		df = pd.read_sql('''SELECT * FROM fc8 WHERE shortcode in ('{}');'''.format(shortcodes_csv[i]), conn)
		df.fc8 = df.fc8.apply(lambda x: np.fromstring(x[1:-1], sep='\n'))
		users_vectors.append(df)

	vectorsums = []
	for i, user in enumerate(sample_users):
		vectorsum = users_vectors[i].fc8.values.sum()
		vectorsums.append(vectorsum)
	# matrix of documents vs words
	# each entry is a word count
	word_counts = np.concatenate([vectorsums[0][np.newaxis,:],
								vectorsums[1][np.newaxis,:],
								vectorsums[2][np.newaxis,:],
								vectorsums[3][np.newaxis,:]], axis=0)
	# calculate document frequency for each word
	# results in a 1000-element array of count of documents
	df = np.sum(word_counts > 0, axis=0)
	# normalize word_count matrix to get term frequencies
	# ie. divide each term frequency by total count of number of words in that document
	tf_norm = np.sqrt((word_counts ** 2).sum(axis=1))
	tf_norm[tf_norm == 0] = 1 # avoid divide by zero
	tf = word_counts / tf_norm.reshape(4,1)
	# inverse document frequency
	idf = np.log((4 + 1.) / (1. + df)) + 1.
	tfidf = tf * idf
	# normalize tfidf matrix by dividing by l2 norm
	tfidf_norm = np.sqrt((tfidf ** 2).sum(axis=1))
	tfidf_norm[tfidf_norm == 0] = 1
	tfidf_normed = tfidf / tfidf_norm.reshape(4,1) # we're working with 4 documents (users)

def get_user_vector_pkls(category):
	tracker_df = pd.read_pickle('./tracker.pkl')
	with open('../data/{}.txt'.format(category), 'r') as f:
		lines = f.readlines()
		lines = [l for l in lines if not l.startswith('#')]
		users = [l.split('\n')[0] for l in lines]

	shortcodes = []
	for user in users:
		print user
		user_df = tracker_df[tracker_df.username == user]
		user_df = user_df[user_df.predicted == 1]

		shorts = user_df.shortcode.values
		shortcodes.append(shorts)

	shortcodes_csv = map(lambda x: "','".join(x), shortcodes)

	users_vectors = []
	for user, shorts in zip(users, shortcodes_csv):
		df7 = pd.read_sql('''SELECT * FROM fc7 WHERE shortcode IN ('{}');'''.format(shorts), conn)
		df8 = pd.read_sql('''SELECT * FROM fc8 WHERE shortcode IN ('{}');'''.format(shorts), conn)
		smax = pd.read_sql('''SELECT * FROM softmax WHERE shortcode IN ('{}');'''.format(shorts), conn)
		print 'df7: ', df7.shape
		print 'df8: ', df8.shape
		print 'smax: ', smax.shape

		df7.fc7 = df7.fc7.apply(lambda x: np.fromstring(x[1:-1], sep='\n'))
		df8.fc8 = df8.fc8.apply(lambda x: np.fromstring(x[1:-1], sep='\n'))
		smax.softmax = smax.softmax.apply(lambda x: np.fromstring(x[1:-1], sep='\n'))

		fname7 = './fc7_{}.pkl'.format(user)
		fname8 = './fc8_{}.pkl'.format(user)
		fnamesmax = './smax_{}.pkl'.format(user)

		df7.to_pickle(fname7)
		df8.to_pickle(fname8)
		smax.to_pickle(fnamesmax)
	return

def vector_to_document(vector):
	# convert vector to integers to avoid confusion
	vector = vector.astype(int)
	# use zfill to pad strings with zeros. '1'.zfill(3) == '001'
	list_of_words = [['{}'.format(i).zfill(4)]*j for i,j in enumerate(vector)]
	# flatten the list
	list_of_words = [item for sublist in list_of_words for item in sublist]
	# put everything into one string to represent a document
	document = ' '.join(list_of_words)
	return document

def pilot_test():
	users_vectors = []
	vectorsums = []
	for i, user in enumerate(sample_users):
		# df = pd.read_pickle('./fc8_10imgs_{}.pkl'.format(user))
		df = pd.read_pickle('./fc8_100imgs_{}.pkl'.format(user))
		users_vectors.append(df)
		vectorsums.append(df.fc8.values.sum())

	corpus = []
	for vector in vectorsums:
		corpus.append(vector_to_document(vector))

	tfidf = TfidfVectorizer()
	tfidf_vectorized = tfidf.fit_transform(corpus)

	cosine_similarities = linear_kernel(tfidf_vectorized, tfidf_vectorized)

	new_docs = []
	for i, user in enumerate(sample_users):
		for j, img_vec in enumerate(users_vectors[i].fc8):
			doc = vector_to_document(img_vec)
			new_docs.append(doc)
			# vectorized = tfidf.transform([doc])
			# sims = linear_kernel(vectorized, tfidf_vectorized)[0]
			# most_sims = np.argsort(sims)[::-1]
			#
			# print '{} img {} most similar to \n{}'.format(user, j, [(sample_users[i], sims[i]) for i in most_sims] )

	new_docs_vectorized = tfidf.transform(new_docs)
	cosine_similarities = linear_kernel(new_docs_vectorized, tfidf_vectorized)

	for sim in cosine_similarities:
		print 'top score: {}     top user: {}'.format(sim.max(), sample_users[np.argmax(sim)])

def make_user_category_dict():
	categories = ['cats', 'dogs', 'foodies', 'models',
					'photographers', 'travel', 'most_popular']

	user_cat_dict = {}
	for categ in categories:
		with open('../data/{}.txt'.format(categ), 'r') as f:
			lines = f.readlines()
			lines = [l for l in lines if not l.startswith('#')]
			usernames = [l.split('\n')[0] for l in lines]
			for username in usernames:
				user_cat_dict[username] = categ
	return user_cat_dict

user_cat_dict = make_user_category_dict()

def pilot_test3(users_per_group=50, feat_type='fc8'):
	categories = ['cats', 'dogs', 'foodies', 'models',
					'photographers', 'travel', 'most_popular']
	lines = []
	for categ in categories:
	# for categ in ['cats', 'dogs', 'foodies', 'models']:
		with open('../data/{}.txt'.format(categ), 'r') as f:
			rawlines = f.readlines()
			if len(rawlines) < users_per_group:
				subset = rawlines
			else:
				subset = np.random.choice(rawlines, size=users_per_group, replace=False)
			print 'num_users from {}: '.format(categ), len(subset)
			lines.append(subset)

	lines = [item for sublist in lines for item in sublist]
	lines = [l for l in lines if not l.startswith('#')]
	usernames = [l.split('\n')[0] for l in lines]

	vectorsums = []

	if feat_type == 'fc8':
		for i, user in enumerate(usernames):
			df = pd.read_pickle('../fc8_pkls/fc8_{}.pkl'.format(user))
			vectorsums.append(df.fc8.values.sum())

	if feat_type == 'fc7':
		for i, user in enumerate(usernames):
			df = pd.read_pickle('../fc7_pkls/fc7_{}.pkl'.format(user))
			vectorsums.append(df.fc7.values.sum())

	corpus = []
	for i, vector in enumerate(vectorsums):
		print i, usernames[i]
		corpus.append(vector_to_document(vector))

	tfidf = TfidfVectorizer()
	tfidf_vectorized = tfidf.fit_transform(corpus)

	cosine_sims = linear_kernel(tfidf_vectorized, tfidf_vectorized)
	for i, sim in enumerate(cosine_sims):
		top = [usernames[np.argsort(sim)[-j]] for j in xrange(1,5)]

		print user_cat_dict[usernames[i]], '===', usernames[i]
		for j, user in enumerate(top):
			print '\t {}. {} === {}'.format(j, user_cat_dict[user], user)

	return cosine_sims, usernames
