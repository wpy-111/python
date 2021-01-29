"""
    梅尔频率倒谱系数
"""
import numpy as np
import scipy.io.wavfile as wf
import python_speech_features as sf
import matplotlib.pyplot as mp
#得到采样率，和采样位移
sample_rate,sigs = wf.read('apple.wav')
#提取mfcc
mfcc = sf.mfcc(sigs,sample_rate)
mp.imshow(mfcc,camp='jet')
mp.show()