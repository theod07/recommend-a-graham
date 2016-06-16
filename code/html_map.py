import os

USER_GROUPS = ['cats', 'dogs', 'foodies', 'models', 'most_popular', 'photographers', 'travel']

def get_unique_users():
	# store usernames in a set for fast look-up and handle duplicates
	users = set()
	for group in USER_GROUPS:
		# read in the list of users from file
		with open('../data/{}.txt'.format(group), 'r') as f:
			lines = f.readlines()
			lines = [l for l in lines if not l.startswith('#')]
			usernames = [l.split('\n')[0] for l in lines]
		# how many usernames are in this group?
		print 'len({}): {}'.format(group, len(usernames)) 
		for x in usernames:
			# print out duplicates to terminal 
			if x in users:
				print '{} from group {} already in users'.format(x, group)
			# add unique entries to set
			else:
				users.add(x)
	# total unique usernames
	print 'len(users): {}'.format(len(users))
	return users

# mannually go through and comment out the users that are repetitive from the .txt files
# by inserting # to start of line

def make_html_map():
	dirs = {}
	for group in USER_GROUPS:
		ds = [d for d in os.listdir('../data/{}'.format(group)) if d.endswith('files')]
		with open('../data/{}.txt'.format(group), 'r') as f:
			lines = f.readlines()
			lines = [l for l in lines if not l.startswith('#')]
			usernames = [l.split('\n')[0] for l in lines]
		for username in usernames:
			for d in ds:
				if username in d:
					dirs[username] = d
		print 'completed group {}'.format(group)
	print 'len(dirs): {}'.format(len(dirs))

	with open('../data/html_map.txt', 'ab') as f:
		for k in dirs:
			f.write('{}!@#$!@#$!@#$ {}\n'.format(k, dirs[k]))
	return

def user_group_dictionary():
	d = {}
	for group in USER_GROUPS:
		with open('../data/{}.txt'.format(group), 'r') as f:
			lines = f.readlines()
			lines = [l for l in lines if not l.startswith('#')]
			usernames = set([l.split('\n')[0] for l in lines])
		d[group] = usernames
	return d

user_group_dictionary = user_group_dictionary()