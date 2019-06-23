from skimage import filters, io, color
import matplotlib.pyplot as plt

def laplace_filter(image):
	im = io.imread(image, as_gray = True)
	im_new = filters.laplace(im)
	im_new = color.rgb2gray(im_new)
	plt.figure()
	plt.imshow(im_new, cmap='Greys_r')
	plt.savefig('laplacefilter.png')
	plt.show()

if __name__ == '__main__':
	laplace_filter('humanbodycross.png')
