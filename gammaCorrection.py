from skimage import io
import numpy as np
import matplotlib.pyplot as plt

def gamma_correction(image, gamma):
	im = io.imread(image, as_gray = True)
	maximum = np.max(im)
	im_norm = im / maximum
	im_new = np.exp(gamma*np.log(im_norm)) * (pow(2,8)-1)
	plt.figure()
	plt.imshow(im_new, cmap = 'Greys_r')
	plt.axis('off')
	plt.savefig('gammacorrection.png')
	plt.show()

if __name__ == '__main__':
	gamma_correction('vessel.png', .5)
