import os
from bs4 import BeautifulSoup
import pandas as pd

dirs = os.listdir('../data/raw/')
soup = BeautifulSoup(open('../data/raw/{}'.format(dirs[0]), 'r'), 'lxml')
print type(soup)

a_tags = soup.findAll('a')
print len(a_tags)

tag = a_tags[2]
print tag.attrs

print [tag.attrs for tag in a_tags]

def get_hrefs_srcs(fname):
	"""
	take in a html file and return the hrefs and img_src links
	"""
	with open('../data/raw/{}'.format(fname), 'r') as f:
		soup = BeautifulSoup(f, 'lxml')

	a_tags = soup('a')
	hrefs, srcs = [], []
	for tag in a_tags:
		if tag('img'):
			hrefs.append(tag['href'])
			srcs.append(tag('img')[0]['src'])
	if len(hrefs) != len(srcs): print 'len(hrefs): {},  len(srcs): {}'.format(len(hrefs), len(srcs))
	return hrefs, srcs

def href_to_shortcode(hrefs):
	shortcodes = []
	for href in hrefs:
		left = href.split('/?taken-by=')[0]
		shortcodes.append(left.split('instagram.com/p/')[-1])
	# username = href.split('/?taken-by=')[-1]
	return shortcodes #, username

def src_to_img_id(srcs):
	img_ids = []
	for src in srcs:
		img_ids.append(src.split('/')[-1])
	return img_ids

def save_df(username, shortcodes, img_ids)
	if len(shortcodes) != len(img_ids): 
		print 'Fail. len(shortcodes) != len(img_ids) for user: {}'.format(username)
		return
	df = pd.DataFrame(columns=['shortcode', 'img_id'])
	df.shortcode = shortcodes
	df.img_id = img_ids
	df.to_pickle('../data/pickles/{}.pkl'.format(username))
	print 'saved to pickles/{}.pkl'.format(username)

def get_user_from_dirname(dirname):
	loc = dirname.find('@')

	if loc == 0:
		username = dir.split(' ')[0].split('@')[-1]

	else:
		username = dir.split('@')[-1].split(')')[0]

	return username


if __name__ == '__main__':

	dirs = [dir for dir in os.listdir('../data/raw/') if dir.endswith('.html')]

	while len(dirs) > 0:
		fname = dirs.pop()

		# only continue if user.pkl DNE
		if not '{}.pkl'.format(get_user_from_dirname(fname)) in os.listdir('../data/pickles/'):
			hrefs, srcs = get_hrefs_srcs(fname)



# images: 


# # tag
# <a class="_8mlbc _t5r8b" data-reactid=".0.1.0.1:$mostRecentSection/=10.0.$0.$1209734947818499870" href="https://www.instagram.com/p/BDJ14aNGO8e/?taken-by=wakeupandmakeup">
	
# 	<div class="_22yr2" data-reactid=".0.1.0.1:$mostRecentSection/=10.0.$0.$1209734947818499870.0">
	
# 	<div class="_jjzlb" data-reactid=".0.1.0.1:$mostRecentSection/=10.0.$0.$1209734947818499870.0.0">
	
# 		<img alt="Sharp liner \U0001f52a @nikkietutorials" class="_icyx7" data-reactid=".0.1.0.1:$mostRecentSection/=10.0.$0.$1209734947818499870.0.0.$pImage_0" id="pImage_0" src="%23WakeUpAndMakeup%20%28@wakeupandmakeup%29%20%E2%80%A2%20Instagram%20photos%20and%20videos_files/1739360_1755441631353145_2083462979_n.jpg" style=""/>
	
# 	</div>
	
# 	<noscript data-reactid=".0.1.0.1:$mostRecentSection/=10.0.$0.$1209734947818499870.0.1">
# 	</noscript>
	
# 	<div class="_ovg3g" data-reactid=".0.1.0.1:$mostRecentSection/=10.0.$0.$1209734947818499870.0.2">
# 	</div>
	
# 	</div>
	
# 	<div class="_1lp5e" data-reactid=".0.1.0.1:$mostRecentSection/=10.0.$0.$1209734947818499870.1">
	
# 	<div class="_cxj4a _j5wem" data-reactid=".0.1.0.1:$mostRecentSection/=10.0.$0.$1209734947818499870.1.0">
	
# 	<span class="_345gm" data-reactid=".0.1.0.1:$mostRecentSection/=10.0.$0.$1209734947818499870.1.0.0">Video
# 	</span>
	
# 	</div>
	
# 	</div>
# </a>