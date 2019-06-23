import scipy.misc as misc
from scipy.misc.pilutil import Image
from skimage import filters

def prewitt_filter(image):
	im = Image.open(image).convert('L')
	im_new = filters.prewitt(im)
	im_new = misc.toimage(im_new)
	im_new.save('prewittfilter.png')

if __name__ == '__main__':
	prewitt_filter('humanskull.png')
