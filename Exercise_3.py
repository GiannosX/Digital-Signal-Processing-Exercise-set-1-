import numpy as np 
import matplotlib.pyplot as plt 
#A)
Fs_t = 2000
Ts_t = 1/Fs_t
Fs_n = 1200
Ts_n = 1/Fs_n 
total_time = 128*Ts_n

t = np.arange(0,total_time, Ts_t)
x_t = 12*np.cos(2*np.pi*20*t) - 18*np.sin(2*np.pi*60*t + np.pi/6)
n = np.arange(0,total_time, Ts_n)
x_n = 12*np.cos(2*np.pi*20*n) - 18*np.sin(2*np.pi*60*n + np.pi/6)

fig, ax = plt.subplots(1,1,figsize=(14,10))

ax.plot(t,x_t,'--', color='lightgrey',label='x(t)')
ax.stem(n,x_n,label='x[n]')
ax.legend()
ax.grid(True)
ax.set_title("x(t)")
ax.set_xlabel("time (s)")
ax.set_ylabel("Amplitude")

plt.tight_layout()
plt.show()