"""
    随机填充
"""
import numpy as np
import PIL
import random
def random_expand(img,
                  gtboxes,#标注坐标
                  max_ratio = 4,
                  fill = None,
                  keep_ratio = True,
                  thresh = 0.5):
    """随机在图像外围进行填充"""
    #random.random()用于生成一个0到1的随机符点数: 0 <= n < 1.0
    if random.random() > thresh:
        return img,gtboxes
    if max_ratio < 1.0:
        return img,gtboxes
    h,w,c = img.shape
    ratio_x = random.uniform(1,max_ratio)
    if keep_ratio:
        ratio_y = ratio_x
    else:
        ratio_y = random.uniform(1,max_ratio)
    #进行了填充标注的坐标发生了变化
    oh = int(h * ratio_y)
    ow = int(w * ratio_x)
    #random.randit(1,6)随机产生一个数（1，6）
    off_x = random.randint(0,ow-w)
    off_y = random.randint(0,oh-h)
    out_img = np.zeros((oh,ow,c))
    #产生大小为oh*ow新图片，先将数值全部填充为fill指定的数值
    if fill and len(fill) == c:
        for i in range(c):
            out_img[:,:,i] = fill[i]*255.0
    #将原图赋值到新图片对应区域
    out_img[off_y:off_y+h,off_x:off_x+w,:] = img
    gtboxes[:,0] = ((gtboxes[:,0]*w)+off_x) /float(ow)
    gtboxes[:,1] = ((gtboxes[:,1]*h)+off_y) /float(oh)
    gtboxes[:,2] = gtboxes[:,2] /ratio_x
    gtboxes[:,3] = gtboxes[:,3] /ratio_y
    return out_img.astype('uint8'),gtboxes
















