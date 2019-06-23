import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, transform
from scipy.ndimage import gaussian_filter

def gradient_map(image):
	im = io.imread(image)
	im = transform.resize(im, (512,512))
	im = color.rgb2gray(im)
	im = im[:,::2]
	im = im[::2,:]
	im = gaussian_filter(im,sigma=1.0)	
	
	Dx, Dy = np.gradient(im)
	Mag = np.sqrt(Dx**2 + Dy**2)
	#[-pi,pi]
	Dir = np.arctan2(-Dy,Dx) + np.pi
	mask = Dir>=0
	Dir = np.ma.array(Dir,mask=mask) + 2*np.pi
	Dir.mask = np.ma.nomask
	Dir = np.array(Dir)

	plt.figure(figsize=(20,18))
	plt.imshow(im)
	r, c = Dx.shape
	X = range(0,c)
	Y = range(0,r)
#	Y = np.max(Y) - Y
	plt.quiver(X,Y,Dx,Dy,scale=10.,zorder=3,color='red',
				width=0.0007,headwidth=0.005,headlength=0.006)
	plt.savefig('gradient_map.jpg')
	plt.show()

if __name__ == '__main__':
	gradient_map('pic1.jpg')
