import numpy as np 
import matplotlib.pyplot as plt 
#A)
Fs_t = 2000
Ts_t = 1/Fs_t
Fs_n = 1200
Ts_n = 1/Fs_n 
total_time = 128*Ts_n
NFFT = 1024

t = np.arange(0,total_time, Ts_t)
x_t = 12*np.cos(2*np.pi*20*t) - 18*np.sin(2*np.pi*60*t + np.pi/6)
n = np.arange(0,total_time, Ts_n)
x_n = 12*np.cos(2*np.pi*20*n) - 18*np.sin(2*np.pi*60*n + np.pi/6)

X_k = np.abs(np.fft.fftshift(np.fft.fft(x_n,NFFT)*Ts_n))
k = np.fft.fftshift(np.fft.fftfreq(NFFT, d=Ts_n))

fig, ax = plt.subplots(2,1,figsize=(14,10))

ax[0].plot(t,x_t,'--', color='lightgrey',label='x(t)')
ax[0].stem(n,x_n,label='x[n]')
ax[0].legend()
ax[0].grid(True)
ax[0].set_title("x(t)")
ax[0].set_xlabel("time (s)")
ax[0].set_ylabel("Amplitude")
ax[1].plot(k,X_k,label='X[k]')
ax[1].set_xlim(-300,300)
ax[1].legend()
ax[1].grid(True)
ax[1].set_title("Frequency Spectrum")
ax[1].set_xlabel("frequency (Hz)")
ax[1].set_ylabel("Amplitude")

plt.tight_layout()
plt.show()