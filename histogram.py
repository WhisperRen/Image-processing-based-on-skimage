from skimage import io, color
import matplotlib.pyplot as plt
import numpy as np

def histogram(image):
	im = io.imread(image)
	green = im[:,:,1]
	#counts = np.unique(green, return_counts=True)[1]
	green = green.flatten()

	plt.figure(figsize=(10,8))
	plt.hist(x=green,bins=256)
	plt.show()

if __name__ == '__main__':
	histogram('pic1.jpg')
