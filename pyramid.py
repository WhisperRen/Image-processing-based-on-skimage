import numpy as np
from skimage import io, transform
import matplotlib.pyplot as plt

def pyramid(image):
	im = io.imread(image)
	im = transform.resize(im,(512,512))
	r, c, d = im.shape
#	the amount of generated pics is log(512)=9
	pyramid = tuple(transform.pyramid_gaussian(im, downscale=2, multichannel=True))
#	background
	bg = np.ones((r, int(c+c/2), 3), dtype=np.double)
#	original pic fusion
	bg[:r, :c, :] = pyramid[0]

#	looping fusion
	i_row = 0
	for i in pyramid[1:]:
		n_row, n_col = i.shape[:2]
		bg[i_row:i_row+n_row, c:c+n_col] = i
		i_row += n_row
	io.imsave('pyramid.jpg', bg)
	plt.imshow(bg)
	plt.show()

if __name__ == '__main__':
	pyramid('pic1.jpg')
