"""
    图像增多方法
"""
import numpy as np
from t01_color import random_disort
from t02_expand import random_expand
from t03_crop import random_crop
from t04_interp import random_interp
from t05_flip import random_flip
size = 512
def img_augment(img,gtboxes,glables,size,means=None):
    img = random_disort(img)
    img,gtboxes = random_expand(img,gtboxes,fill=means)
    img = random_crop(img,gtboxes,glables)
    img = random_interp(img,size)
    img = random_flip(img,gtboxes)
    #随机打乱真实框排列顺序
    gtboxes,glables = shuffle_gtbox(gtboxes,glables)

    return img.astype('float32'),gtboxes.astype('float32'),glables.astype('int32')

def shuffle_gtbox(gtboxes,glables):
    gt = np.concatenate([gtboxes,glables[:,np.newaxis]],axis=1)
    idx = np.arange(gt.shape[0])
    np.random.shuffle(idx)
    gt = gt[idx,:]

    return gt[:,:4],gt[:,4]