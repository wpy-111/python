"""
    基于FFt频率滤波
"""
# 基于傅里叶变换的频域滤波（降噪）
import numpy as np
import numpy.fft as nf
import scipy.io.wavfile as wf  # 音频处理模块
import matplotlib.pyplot as mp

# 读取音频文件，返回采样率、采样位移
sample_rate, noised_sigs = wf.read("../da_data/noised.wav")  # 读取音频文件
print("sample_rate:", sample_rate)  # 采样率
print("noised_sigs.shape:", noised_sigs.shape)  # 采样位移

# 1. 绘制音频时域时间/位移图像
noised_sigs = noised_sigs / (2 ** 15)  # 缩小位移的范围，用于显示
times = np.arange(noised_sigs.size) / sample_rate  # 计算每个采样点的时间点

mp.figure("Filter", facecolor="lightgray")
mp.subplot(221)
mp.title("Time Domain", fontsize=16)
mp.ylabel("Signal", fontsize=12)
mp.grid(linestyle=":")
mp.plot(times[:178], noised_sigs[:178],  # 只看前178个采样点
        color="dodgerblue", label="Noised")

# 2. 基于傅里叶变化，获取音频频域信息
freqs = nf.fftfreq(times.size, times[1] - times[0])
complex_arr = nf.fft(noised_sigs)  # 傅里叶变换
pows = np.abs(complex_arr)
# 绘制频域能量图像
mp.subplot(222)
mp.title("Frequency Domain", fontsize=16)
mp.ylabel("Power", fontsize=12)
mp.grid(linestyle=":")
mp.semilogy(freqs[freqs > 0], pows[freqs > 0],  # 只看频率大于0的部分
            color="orangered", label="Noised")  # 采用半对数坐标

# 3. 将低能噪声去除，绘制音频/能量图像
# 找到能量最大的采样点的位置，去除其它的
fund_freq = freqs[pows.argmax()]  # 能量最大的频率
noised_idx = np.where(freqs != fund_freq)  # 噪声点的下标
complex_arr[noised_idx] = 0  # 将噪声位置的数据抹掉
pows = np.abs(complex_arr)  # 去噪后的能量数据

mp.subplot(223)
mp.title("Frequency Domain", fontsize=16)
mp.ylabel("Power", fontsize=12)
mp.grid(linestyle=":")
mp.plot(freqs[freqs > 0], pows[freqs > 0],  # 只看频率大于0的部分
        color="orangered", label="Filtered")  # 采用半对数坐标

# 4. 做逆向傅里叶变换，生成降噪后的音频时域图
filter_sigs = nf.ifft(complex_arr)  # 逆向傅里叶变换
mp.subplot(224)
mp.title("Filtered Signal", fontsize=16)
mp.ylabel("Signal", fontsize=12)
mp.grid(linestyle=":")
mp.plot(times[:178], filter_sigs[:178],  # 只看前178个采样点
        color="dodgerblue", label="Filtered")

# 5. 将降噪后的数组还原成音频
wf.write("../da_data/filtered_777.wav",  # 文件路径
         sample_rate,  # 采样率
         (filter_sigs * 2 ** 15).astype(np.int16))  # 数据

mp.tight_layout()
mp.show()





