import pandas as pd
import numpy as np

sample_users = ['goemon16', 'andrew_icant', 'instagramtop50', 'lebackpacker']
tracker_df = pd.read_pickle('./tracker.pkl')

shortcodes = [] # len4 list of len100 lists of shortcodes
for user in sample_users:
	user_df = tracker_df[tracker_df.username == user]
	user_df = user_df[user_df.predicted == 1]
	shorts = np.random.choice(user_df.shortcode.values, size=10, replace=False)
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

def vector_to_document(vector):
	# convert vector to integers to avoid confusion
	vector = vector.astype(int)
	list_of_words = [['{}'.format(i)]*j for i,j in enumerate(vector)]
	list_of_words = [item for sublist in list_of_words for item in sublist]
	document = ' '.join(list_of_words)
	return document
