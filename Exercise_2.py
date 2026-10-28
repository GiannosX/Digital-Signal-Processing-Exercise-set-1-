import numpy as np 
import matplotlib.pyplot as plt 

Ts_t = 1/150 # Sampling Period for the continuous signal x(t)
Ts_n = 1/20 # (α) Sampling Period for the sampled signal x[n]

t = np.arange(0+Ts_t,0.5,Ts_t) # Time array starts from Ts (not from 0) because 0<t<500ms
n = np.arange(0, 0.5, Ts_n)
x_t = 20*np.cos(10*np.pi*t) - 40*np.sin(5*np.pi*t)
x_n = 20*np.cos(10*np.pi*n) - 40*np.sin(5*np.pi*n)
NFFT=1<<int(np.ceil(np.log2(len(x_t))))

X = np.abs(np.fft.fftshift(np.fft.fft(x_t)*Ts_t)) # Frequency domain
f = np.fft.fftshift(np.fft.fftfreq(len(x_t),d=Ts_t))

fig, ax = plt.subplots(2,2)
ax[0][0].plot(f,X)
ax[0][0].set_title("X(f)")
ax[0][0].grid(True)

ax[0][1].plot(t,x_t, '--', color='lightgrey')
ax[0][1].stem(n,x_n)
ax[0][1].set_title(f"Sampled signal with Ts = {Ts_n}")
ax[0][1].grid(True)
#Reconstruct the sampled signal for Sampling Period = 1/10
Ts_n = 1/10 # (β)
n = np.arange(0, 0.5, Ts_n)
x_n = 20*np.cos(10*np.pi*n) - 40*np.sin(5*np.pi*n)

ax[1][0].plot(t,x_t, '--', color='lightgrey')
ax[1][0].stem(n,x_n)
ax[1][0].set_title(f"Sampled signal with Ts = {Ts_n}")
ax[1][0].grid(True)
#Reconstruct the sampled signal for Sampling Period = 1/10
Ts_n = 1/5 # (γ)
n = np.arange(0, 0.5, Ts_n)
x_n = 20*np.cos(10*np.pi*n) - 40*np.sin(5*np.pi*n)

ax[1][1].plot(t,x_t, '--', color='lightgrey')
ax[1][1].stem(n,x_n)
ax[1][1].set_title(f"Sampled signal with Ts = {Ts_n}")
ax[1][1].grid(True)

plt.show()