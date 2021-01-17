"""
     超几何分布
"""
import numpy as np
# 从6个好球、4个坏球中抽取3个球，返回好球的数量（执行10次）
r = np.random.hypergeometric(6,4,3,10)
b = np.random.hypergeometric(6,4,3,1000000)
for i in range(4):
    print(i,':',(b==i).sum()/1000000)