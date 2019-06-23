from skimage import io
import matplotlib.pyplot as plt
import numpy as np

def contrast_stretching(image):
	im = io.imread(image, as_gray = True)
	im = im*(pow(2,8)-1)

	a = im.min()
	b = im.max()
	print(a, b)
	im_new = (pow(2,8)-1) * (im-a) / (b-a)
	im_new = im_new.astype('uint8')

	plt.figure()
	plt.imshow(im_new, cmap = 'Greys_r')
	plt.axis('off')
	plt.savefig('contraststretching.png')
	plt.show()

if __name__ == '__main__':
	contrast_stretching('vessel.png')
