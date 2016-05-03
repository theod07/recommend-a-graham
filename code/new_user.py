import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.io import imshow


def get_user_preference(imgs):
	'''
	Display images to new_user and prompt for response (Like/NoLike)
	Keep track of preferences in a list.
	
	INPUT: list of pairs, (username, img_id)

	OUTPUT: list of new_user's preferences (zero or one)
	'''
	prefs = []
	for img in imgs:
		imshow(img)
		pref = raw_input('Like? 1   No Like? 0')
		prefs.append(pref)
	return prefs


def random_pick_imgs(categories):
	'''
	Randomly select 10 imgs from each category to be shown to new user.
	INPUT: None
	
	OUTPUT: list of lists of images.
	'''
	imgs = []
	for cat in categories:
		choices = np.random.choice(os.listdir('../imgs/{}'.format(cat)), size=10, replace=False)
		imgs.append(choices)

	return imgs

def new_user_softmax_mean(imgs, conn):
	q1 = '''
		SELECT username, 
				shortcode, 
				predicted
		FROM tracker
		WHERE img_id IN ('{}');
		'''.format("','".join(imgs))
	
	df = pd.read_sql(q1, conn)
	return df


if __name__ == '__main__':

	CATEGORIES = ['cats', 'dogs']

	imgs = random_pick_imgs(CATEGORIES)
	prefs = get_user_preferences(imgs)


	# user_short_pred_df = new_user_softmax_mean(imgs, conn)