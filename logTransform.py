from skimage import io
import numpy as np
import matplotlib.pyplot as plt

def log_transform(image):
	im = io.imread(image, as_gray = True)
	k = (pow(2,8)-1) / np.log(1 + np.max(np.abs(im)))
	im_new = k * np.log(1 + im)
	plt.figure()
	plt.imshow(im_new, cmap='Greys_r')
	plt.axis('off')
	plt.show()
	plt.savefig('logtransform.png')

if __name__ == '__main__':
	log_transform('electronScope.png')
