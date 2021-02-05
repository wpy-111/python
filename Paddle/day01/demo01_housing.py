"""
    波士顿房价预测
"""
import numpy as np
import paddle
import paddle.fluid as fluid
import paddle.fluid.dygraph as dygraph #动态图加载
from paddle.fluid.dygraph import Linear
import os
import random


