"""
    随机裁剪
"""
import numpy as np

def random_crop(img,
                boxes,
                labels,
                scales = [0.3,1.0],
                max_ratio = 2.0,
                constraints = None,
                max_trail = 50):
    if not constraints:
        constraints = [(0.1,1.0),(0.3,1.0),(0.5,1.0),(0.7,1.0),(0.9,1.0),(0.0,1.0)]