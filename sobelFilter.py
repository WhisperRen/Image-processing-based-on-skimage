import scipy.misc as misc
from scipy.misc.pilutil import Image
from skimage import filters

def sobel_filter(image):
	im = Image.open(image).convert('L')
	im_new = filters.sobel(im)
	im_new = misc.toimage(im_new)
	im_new.save('sobelfilter.png')

if __name__ == '__main__':
	sobel_filter('humanskull.png')
