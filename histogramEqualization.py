import numpy as np
import matplotlib.pyplot as plt
from skimage import io

def histogram_equalization(image):
	im = io.imread(image, as_gray = True)
	
	# the operation should be done for normalized image in dtype float
	im_1d = (pow(2,8)-1) * im.flatten()
	im_1d = im_1d.astype('uint8')
	
	# hist is the value, bins is the x tick
	hist, bins = np.histogram(im_1d, 256, [0, 255])
	
	# compute CDF by applying accumulation on hist
	cdf = hist.cumsum()
	
	# np.ma 掩码数组模块 (masked array), 
	#invalid specified values in the array
	cdf_m = np.ma.masked_equal(cdf, 0)
	
	# compute the transform function
	num_cdf_m = (cdf_m - cdf_m.min()) * (pow(2,8)-1)
	den_cdf_m = (cdf_m.max() - cdf_m.min())
	cdf_m = num_cdf_m / den_cdf_m
	
	# fill the masked value by zero
	cdf = np.ma.filled(cdf_m, 0).astype('uint8')
	im2 = cdf[im_1d]
	im_new = np.reshape(im2, im.shape)
	
	plt.figure()
	plt.imshow(im_new, cmap = 'Greys_r')
#	plt.axis('off')
#	plt.savefig('histogramequalization.png')
	plt.show()

if __name__ == '__main__':
	histogram_equalization('lungs.png')
