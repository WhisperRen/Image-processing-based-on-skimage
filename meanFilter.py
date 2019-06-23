import numpy as np
import scipy.ndimage.filters as filters
import scipy.misc as misc
from scipy.misc.pilutil import Image

def mean_filter(image, filter_size):
	im = Image.open(image).convert('L')

	# convert image to a numpy array
	im_matrix = misc.fromimage(im)

	# initialize the kernel of size 5-by-5
	k = np.ones((filter_size,filter_size))/(filter_size**2)
	im_meanfilter = filters.convolve(im, k, mode='nearest')

	# convert array to image
	image_new = misc.toimage(im_meanfilter)

	image_new.save('meanfilter.png')

if __name__ == '__main__':
	mean_filter('saltpepper.png', 5)
