from skimage import io
import matplotlib.pyplot as plt

def inverse_transform(image):
	im = io.imread(image, as_gray = True)
	im_new = pow(2,8)-1 - im
	plt.figure()
	plt.imshow(im_new, cmap='Greys_r')
	plt.axis('off')
	plt.savefig('inversetransform.png')
	plt.show()

if __name__ == '__main__':
	inverse_transform('heartCT.png')
