import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from scipy.ndimage import gaussian_filter

def scale_space(image, sigma):
	im = io.imread(image)
	im_blur = gaussian_filter(im, sigma=sigma)
#	io.imsave( 'scale1.jpg', im_blur)
	plt.figure()
	plt.imshow(im_blur)
	plt.show()
if __name__ == '__main__':
	scale_space('pic1.jpg', 4.0)
