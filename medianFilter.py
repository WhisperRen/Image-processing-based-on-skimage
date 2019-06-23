import scipy.misc as misc
import scipy.ndimage.filters as filters
from scipy.misc.pilutil import Image

def median_filter(image, size):
	im = Image.open(image).convert('L')
	im = misc.fromimage(im)
	im_new = filters.median_filter(im, size=size, mode='reflect')
	im_new = misc.toimage(im_new)
	im_new.save('medianfilter.png')

if __name__ == '__main__':
	median_filter('saltpepper.png',5)
