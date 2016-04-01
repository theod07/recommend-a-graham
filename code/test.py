from vgg16_cpu import vgg16
import os

nnet = vgg16()

def get_dirmap():
	with open('../data/html_map.txt', 'r') as f:
		lines = f.read().splitlines()
	dirs = {}
	for line in lines:
		kv = line.split('!@#$!@#$!@#$ ')
		dirs[kv[0]] = kv[1]
	return dirs

dirmap = get_dirmap()
username = 'noelcapri'
print dirmap[username]
print u'{}'.format(dirmap[username].decode('UTF-8'))

imgs = [f for f in os.listdir(u'../data/models/{}'.format(dirmap[username].decode('UTF-8'))) if f.endswith('.jpg')]
print len(imgs)
print imgs[0]
print imgs[0].decode('UTF-8')


user_dir = dirmap[username].decode('UTF-8')
img_name = imgs[0].decode('UTF-8')
path = u'../data/models/{}/{}'.format(user_dir, img_name)

a,b,c = nnet.predict(path)
print a.shape
print b.shape
print c.shape

print a
print b
print c