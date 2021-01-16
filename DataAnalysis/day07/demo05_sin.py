"""
    合成方波 fft
"""
import numpy as np
import matplotlib.pyplot as mp
x = np.linspace(0,4*np.pi,1000)
y = np.zeros_like(x)
for n in range(1,1000):
    y += 4*np.pi / (2*n-1) * np.sin((2*n-1)*x)
#针对y做fft变化
import numpy.fft as nf
complex_ary = nf.fft(y)
y2 = nf.ifft(complex_ary)
#绘制时域图
mp.figure('FFT',facecolor='lightgrey')
mp.subplot(121)
mp.title('time Domain',fontsize=16)
mp.xlabel('Time',fontsize=14)
mp.ylabel('Pow',fontsize=14)
mp.grid(linestyle=':')
mp.plot(x,y,color='dodgerblue',alpha=0.3,linewidth=5,label='y')
mp.plot(x,y2,color='dodgerblue',alpha=1,linewidth=1,label='y2')
mp.legend()
mp.tight_layout()
freqs = nf.fftfreq(len(y),x[1]-x[0])
#abs求绝对值
pow =np.abs(complex_ary)

print(pow)
mp.subplot(122)
mp.title('Frequency Domain',fontsize=16)
mp.xlabel('Frequency',fontsize=14)
mp.ylabel('Pow',fontsize=14)
mp.plot(freqs[freqs>0],pow[freqs>0],color='orangered')

mp.grid(linestyle=':')
mp.tight_layout()
mp.show()