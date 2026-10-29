import numpy as np 
import matplotlib.pyplot as plt 

Fs = 20000
Ts = 1/Fs 
TOTAL_TIME = 1.0
F0 = 500 #frequency range from 500 Hz to 2000 Hz
phi = 0 # phase set to 0 
NFFT = 1<<18 #Large number of samples (2^18) to the frequency domain to avoid scalloping loss 

t = np.arange(0,TOTAL_TIME+Ts, Ts)

fig, ax = plt.subplots(2,1,figsize=(13,10))
# Plot for the Frequency ranges 500-2000
for i in range(4):
    x_t = np.sin(2*np.pi*(i+1)*F0*t + phi)
    X = np.abs(np.fft.fftshift(np.fft.fft(x_t,NFFT)*Ts))
    f = np.fft.fftshift(np.fft.fftfreq(NFFT, d=Ts))
    ax[0].plot(f,X,label=f'X(f) for {(i+1)*500} Hz sinusoid')
ax[0].grid(True)
ax[0].set_xlim(-3000,3000)
ax[0].set_title("Frequency Domain")
ax[0].set_xlabel("Frequency (Hz)")
ax[0].set_ylabel("Amplitude")
ax[0].legend()

#Plot for the Frequency ranges 1800-1950
F0 = 18000
for i in range(4):
    x_t = np.sin(2*np.pi*(F0 + i*500)*t + phi)
    X = np.abs(np.fft.fftshift(np.fft.fft(x_t,NFFT)*Ts))
    f = np.fft.fftshift(np.fft.fftfreq(NFFT, d=Ts))
    ax[1].plot(f,X,label=f'X(f) for {F0 + i*500} Hz sinusoid')
ax[1].grid(True)
ax[1].set_xlim(-3000,3000)
ax[1].set_title("Frequency Domain")
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_ylabel("Amplitude")
ax[1].legend()

plt.tight_layout()
plt.show()
