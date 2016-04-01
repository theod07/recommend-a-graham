# VGG-16, 16-layer model from the paper:
# "Very Deep Convolutional Networks for Large-Scale Image Recognition"
# Original source: https://gist.github.com/ksimonyan/211839e770f7b538e2d8
# License: non-commercial use only

# Download pretrained weights from:
# https://s3.amazonaws.com/lasagne/recipes/pretrained/imagenet/vgg16.pkl

import lasagne
from lasagne.layers import InputLayer
from lasagne.layers import DenseLayer
from lasagne.layers import NonlinearityLayer
from lasagne.layers import DropoutLayer
from lasagne.layers import Pool2DLayer as PoolLayer
# from lasagne.layers.dnn import Conv2DDNNLayer as ConvLayer
from lasagne.layers import Conv2DLayer as ConvLayer
from lasagne.nonlinearities import softmax
import cPickle as pickle
import numpy as np 
import os
import time
import matplotlib.pyplot as plt
import skimage.transform
from lasagne.utils import floatX
import urllib
import io
np.set_printoptions(threshold=np.nan)


class vgg16(object):

    def __init__(self):
        self.model = pickle.load(open('./vgg16.pkl'))
        self.CLASSES = self.model['synset words']
        self.MEAN_IMAGE = self.model['mean value'][:, np.newaxis, np.newaxis]
        self.nnet = self.build_model()
        lasagne.layers.set_all_param_values(self.nnet['prob'], self.model['param values'])

    def build_model(self):
        net = {}
        net['input'] = InputLayer((None, 3, 224, 224))
        net['conv1_1'] = ConvLayer(
            net['input'], 64, 3, pad=1, flip_filters=True)
        net['conv1_2']  = ConvLayer(
            net['conv1_1'], 64, 3, pad=1, flip_filters=True)
        net['pool1'] = PoolLayer(net['conv1_2'], 2)
        net['conv2_1'] = ConvLayer(
            net['pool1'], 128, 3, pad=1, flip_filters=True)
        net['conv2_2'] = ConvLayer(
            net['conv2_1'], 128, 3, pad=1, flip_filters=True)
        net['pool2'] = PoolLayer(net['conv2_2'], 2)
        net['conv3_1'] = ConvLayer(
            net['pool2'], 256, 3, pad=1, flip_filters=True)
        net['conv3_2'] = ConvLayer(
             net['conv3_1'], 256, 3, pad=1, flip_filters=True)
        net['conv3_3'] = ConvLayer(
            net['conv3_2'], 256, 3, pad=1, flip_filters=True)
        net['pool3'] = PoolLayer(net['conv3_3'], 2)
        net['conv4_1'] = ConvLayer(
            net['pool3'], 512, 3, pad=1, flip_filters=True)
        net['conv4_2'] = ConvLayer(
            net['conv4_1'], 512, 3, pad=1, flip_filters=True)
        net['conv4_3'] = ConvLayer(
            net['conv4_2'], 512, 3, pad=1, flip_filters=True)
        net['pool4'] = PoolLayer(net['conv4_3'], 2)
        net['conv5_1'] = ConvLayer(
            net['pool4'], 512, 3, pad=1, flip_filters=True)
        net['conv5_2'] = ConvLayer(
            net['conv5_1'], 512, 3, pad=1, flip_filters=True)
        net['conv5_3'] = ConvLayer(
            net['conv5_2'], 512, 3, pad=1, flip_filters=True)
        net['pool5'] = PoolLayer(net['conv5_3'], 2)
        net['fc6'] = DenseLayer(net['pool5'], num_units=4096)
        net['fc6_dropout'] = DropoutLayer(net['fc6'], p=0.5)
        net['fc7'] = DenseLayer(net['fc6_dropout'], num_units=4096)
        net['fc7_dropout'] = DropoutLayer(net['fc7'], p=0.5)
        net['fc8'] = DenseLayer(
            net['fc7_dropout'], num_units=1000, nonlinearity=None)
        net['prob'] = NonlinearityLayer(net['fc8'], softmax)

        return net

    def prep_image(self, img_path, local_img=True):
        ext = img_path.split('.')[-1]

        if local_img:
            im = plt.imread(img_path)
        else: 
            im = plt.imread(io.BytesIO(urllib.urlopen(img_path).read()), ext)

        # Resize so smallest dim = 256, preserving aspect ratio
        h, w, _ = im.shape
        if h < w:
            im = skimage.transform.resize(im, (256, w*256/h), preserve_range=True)
        else:
            im = skimage.transform.resize(im, (h*256/w, 256), preserve_range=True)

        # Central crop to 224x224
        h, w, _ = im.shape
        im = im[h//2-112:h//2+112, w//2-112:w//2+112]

        rawim = np.copy(im).astype('uint8')

        # Shuffle axes to c01
        im = np.swapaxes(np.swapaxes(im, 1, 2), 0, 1)

        # Convert to BGR
        im = im[::-1, :, :]

        im = im - self.MEAN_IMAGE
        return rawim, floatX(im[np.newaxis])

    def predict(self, img_path, local_img=True):
        tic = time.clock()
        rawim, im = self.prep_image(img_path, local_img)

        print 'calculating probs..'
        prob = np.array(lasagne.layers.get_output(self.nnet['prob'], im, deterministic=True).eval())
        fc8 = np.array(lasagne.layers.get_output(self.nnet['fc8'], im, deterministic=True).eval())
        fc7 = np.array(lasagne.layers.get_output(self.nnet['fc7'], im, deterministic=True).eval())

        print 'got probs..'
        top = np.argsort(prob[0])[-1:-4:-1]
        # print 'preparing to plot'
        # plt.figure()
        # plt.imshow(rawim.astype('uint8'))
        # plt.axis('off')
        # print 'successfully plotted'
        toc = time.clock()

        return prob[0], fc8[0], fc7[0]

if __name__ == '__main__':

    nnet = vgg16()

    imgs = [f for f in os.listdir('.') if f.endswith('.jpg')]

    probs, fc8s, fc7s = [], [], []
    for img in imgs:
        prob, fc8, fc7 = nnet.predict('{}'.format(img), local_img=True)
        probs.append(prob)
        fc8s.append(fc8)
        fc7s.append(fc7)




