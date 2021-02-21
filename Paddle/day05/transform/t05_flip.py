"""
    随机反转
"""
import random
def random_flip(img,gtboxes,thresh=0.5):
    if random.random()>thresh:
        img = img[:,::-1,:]
        gtboxes[:,0] = 1.0 - gtboxes[:,0]
    return img,gtboxes