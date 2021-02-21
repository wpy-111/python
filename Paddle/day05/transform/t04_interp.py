"""
    随机缩放
"""
import cv2 as cv
import random
def random_interp(img,size,interp=None):
    interp_method = [cv.INTER_NEAREST,
                     cv.INTER_LINEAR,
                     cv.INTER_AREA,
                     cv.INTER_CUBIC,
                     cv.INTER_LANCZOS4]
    if not interp or interp not in interp_method:
        interp = interp_method[random.randint(0,len(interp_method)-1)]
        h,w,_ = img.shape
        im_scale_x = size/float(w)
        im_scale_y = size/float(h)
        img = cv.resize(img,None,None,fx=im_scale_x,fy=im_scale_y,interpolation=interp)

    return img