"""
    随机改变亮度，对比度，颜色
"""
import numpy as np
from PIL import ImageEnhance
from PIL import Image
def random_disort(img):
    """随机改变亮度，对比度，颜色"""
    def random_brightness(img,lower=0.5,upper=1.5):
        """亮暗"""
        e = np.random.uniform(lower,upper)
        return ImageEnhance.Brightness(img).enhance(e)
    def random_constract(img,lower=0.5,upper=1.5):
        """对比度"""
        e = np.random.uniform(lower,upper)
        return ImageEnhance.Contrast(img).enhance(e)
    def random_color(img,lower=0.5,upper=1.5):
        """颜色"""
        e = np.random.uniform(lower,upper)
        return ImageEnhance.Color(img).enhance(e)
    #随机打乱操作顺序
    ops = [random_color,random_constract,random_brightness]
    np.random.shuffle(ops)

    img = Image.fromarray(img)
    img = ops[0](img)
    img = ops[1](img)
    img = ops[2](img)
    img = np.asarray(img)
    return img


