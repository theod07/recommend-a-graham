import os

USER_GROUPS = ['cats', 'dogs', 'foodies', 'models', 'most_popular', 'photographers', 'travel']

def get_unique_users():
	"""
	the original list of usernames for each group may have overlaps.
	determine the set of unique usernames across all groups.
	"""
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
	"""
	foldername/directory for each user is not the same as their username
	each directory is a customized name, determined by user.
	use this function to generate a dictionary that holds the string 
	directory name for users
	"""
	dirs = {}
	for group in USER_GROUPS:
		# filter out irrelevant directories
		ds = [d for d in os.listdir('../data/{}'.format(group)) if d.endswith('files')]
		# read in usernames from file
		with open('../data/{}.txt'.format(group), 'r') as f:
			lines = f.readlines()
			lines = [l for l in lines if not l.startswith('#')]
			usernames = [l.split('\n')[0] for l in lines]
		# scan through directories for the string that contains a given username	
		for username in usernames:
			for d in ds:
				if username in d:
					# add the winning (username,directoryname) pair to dictionary
					dirs[username] = d
		# status update to terminal
		print 'completed group {}'.format(group)
	# how many items are in the resulting dictionary?
	print 'len(dirs): {}'.format(len(dirs))
	# write the results to file
	with open('../data/html_map.txt', 'ab') as f:
		for k in dirs:
			# some directories have stupid encoding...
			# make up our own "encoding" as a delimiter
			f.write('{}!@#$!@#$!@#$ {}\n'.format(k, dirs[k]))
	return

def user_group_dictionary():
	"""
	create a dictionary that holds all usernames for a given 
	user category
	"""
	d = {}
	# scan through each group
	for group in USER_GROUPS:
		# read usernames from file
		with open('../data/{}.txt'.format(group), 'r') as f:
			lines = f.readlines()
			lines = [l for l in lines if not l.startswith('#')]
			usernames = set([l.split('\n')[0] for l in lines])
		# assign to dictionary
		d[group] = usernames
	return d

user_group_dictionary = user_group_dictionary()