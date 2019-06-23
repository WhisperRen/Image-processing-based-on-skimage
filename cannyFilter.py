from skimage import feature, io
import matplotlib.pyplot as plt

def canny_filter(image):
	im = io.imread(image, as_gray=True)
	im_new = feature.canny(im, sigma=1)
	plt.figure()
	plt.imshow(im_new, cmap='Greys_r')
	#plt.axis('off')
	#plt.savefig('canny_skull.png')
	plt.show()

if __name__ == '__main__':
	canny_filter('pic1.jpg')
