import numpy as np
from skimage import io
import matplotlib.pyplot as plt

def test_fft2(image):
	im = io.imread(image, as_gray = True)
	im = im * (pow(2,8) - 1)

	im_new = abs(np.fft.fft2(im))
	im_new = abs(np.fft.ifft2(im_new))
	im_new = np.fft.fftshift(im_new)

	plt.figure()
	plt.imshow(im_new, cmap = 'Greys_r')
	plt.axis('off')
	plt.savefig('test_fft2.png')
	plt.show()

if __name__ == '__main__':
	test_fft2('fft.png')
