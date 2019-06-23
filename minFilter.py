import scipy.misc as misc
from scipy.misc.pilutil import Image
import scipy.ndimage.filters as filters

def min_filter(image, size):
	im = Image.open(image).convert('L')
	im_new = filters.minimum_filter(im, size=size, mode='reflect')
	im_new = misc.toimage(im_new)
	im_new.save('minfilter.png')

if __name__ == '__main__':
	min_filter('blackborder.png',5)
