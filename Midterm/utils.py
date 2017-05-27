def imResize(img, scale):
	import cv2
	newx,newy = img.shape[1]/scale,img.shape[0]/scale #new size (w,h)
	newimage = cv2.resize(img,(newx,newy))
	return newimage
