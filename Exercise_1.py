import numpy as np 
import matplotlib.pyplot as plt 

# x[n]
nx = np.arange(-4,5)
x = 10-nx

# y[n]
ny = np.arange(-2,6)
y = 0.8**(ny+1)

# z[n] = x[n]*y[n]
z = np.convolve(x,y,mode='full')
nz = nx[0] + ny[0] + np.arange(len(z))

N = len(x) + len(y) + 1 #Length for all frequency domain signals

# add zero padding to all FFTs to length N 
X = np.fft.fft(x, n=N)
Y = np.fft.fft(y, n=N)
Z = np.fft.fft(z, n=N)
freq = np.fft.fftshift(np.fft.fftfreq(N))

#take the product of the ffts of X and Y to see if its the same as the fft of  x * y (convolution)
Z_product = X*Y 

#shift and take the absolute of the ffts for plotting
X_shifted = np.abs(np.fft.fftshift(X))
Y_shifted = np.abs(np.fft.fftshift(Y))
Z_shifted = np.abs(np.fft.fftshift(Z))
Z_product_shifted = np.abs(np.fft.fftshift(Z_product))

#plots
fig, ax = plt.subplots(2, 2, figsize=(14,20))
ax[0][0].plot(nx,x)
ax[0][0].set_title("x[n]")
ax[0][0].grid(True)
ax[0][1].plot(ny,y)
ax[0][1].set_title("y[n]")
ax[0][1].grid(True)
ax[1][0].plot(nz,z)
ax[1][0].set_title("x[n]*y[n]")
ax[1][0].grid(True)
ax[1][1].plot(freq, X_shifted, label='X(f)', color='blue')
ax[1][1].plot(freq, Y_shifted, label='Y(f)', color='green')
ax[1][1].plot(freq, Z_shifted, label='Z(f)', color='orange')
ax[1][1].plot(freq, Z_product_shifted, '*', label='X(f)*Y(f)', color='r')
ax[1][1].set_title("Frequency domain")
ax[1][1].grid(True)
ax[1][1].legend()

plt.tight_layout()
plt.show()


