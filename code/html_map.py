import os

USER_GROUPS = ['cats', 'dogs', 'foodies', 'models', 'most_popular', 'photographers', 'travel']

users = set()
for group in USER_GROUPS:
	with open('../data/{}.txt'.format(group), 'r') as f:
		lines = f.readlines()
		lines = [l for l in lines if not l.startswith('#')]
		usernames = [l.split('\n')[0] for l in lines]
	print 'len({}): {}'.format(group, len(usernames)) 
	for x in usernames:
		if x in users:
			print '{} from group {} already in users'.format(x, group)
		else:
			users.add(x)
print 'len(users): {}'.format(len(users))

# go through and comment out the users that are repetitive from the .txt files

dirs = {}
for group in USER_GROUPS:
	ds = [d for d in os.listdir('../data/{}'.format(group)) if d.endswith('.html')]
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
		f.write('{}, {}\n'.format(k, dirs[k]))
