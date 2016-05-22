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

word_counts = np.concatenate([vectorsums[0][np.newaxis,:], 
							vectorsums[1][np.newaxis,:],
							vectorsums[2][np.newaxis,:], 
							vectorsums[3][np.newaxis,:]], axis=0)
# calculate document frequency for each word
# results in a 1000-element array of count of documents
df = np.sum(word_counts > 0, axis=0)
