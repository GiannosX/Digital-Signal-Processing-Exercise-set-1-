import numpy as np 
import matplotlib.pyplot as plt 

# x[n]
nx = np.arange(-4,5)
x = 10-nx

# y[n]
ny = np.arange(-2,6)
y = 0.8**(ny+1)

# Manual Convolution based on the formula
len_x = len(x)
len_y = len(y)
len_z = len_x + len_y - 1
z_manual = np.zeros(len_z)

# z[n] = Σ x[k]y[n-k]
for n in range(len_z):
    for k in range(len_x):
        if 0 <= n - k < len_y:
            z_manual[n] += x[k] * y[n - k]

nz = nx[0] + ny[0] + np.arange(len_z)

# Confirmation with numpy.convolve 
z_numpy = np.convolve(x, y, mode='full')
# Print confirmation
is_correct = np.allclose(z_manual, z_numpy)
print(f"Confirmation of Results of the two Convolutions (Manual vs Numpy): {is_correct}")

z = z_manual 

N = len(x) + len(y) + 1 # Length for all frequency domain signals

# Add zero padding to all FFTs to length N 
X = np.fft.fft(x, n=N)
Y = np.fft.fft(y, n=N)
Z = np.fft.fft(z, n=N)
freq = np.fft.fftshift(np.fft.fftfreq(N))

# Take the product of the ffts of X and Y to see if its the same as the fft of x * y (convolution)
Z_product = X * Y 

# Shift and take the absolute of the ffts for plotting
X_shifted = np.abs(np.fft.fftshift(X))
Y_shifted = np.abs(np.fft.fftshift(Y))
Z_shifted = np.abs(np.fft.fftshift(Z))
Z_product_shifted = np.abs(np.fft.fftshift(Z_product))

# Plots
fig, ax = plt.subplots(2, 2, figsize=(14,10))

ax[0][0].stem(nx, x)
ax[0][0].set_title("x[n]")
ax[0][0].grid(True)
ax[0][0].set_xlabel("n")
ax[0][0].set_ylabel("Amplitude")

ax[0][1].stem(ny, y)
ax[0][1].set_title("y[n]")
ax[0][1].grid(True)
ax[0][1].set_xlabel("n")
ax[0][1].set_ylabel("Amplitude")

ax[1][0].stem(nz, z)
ax[1][0].set_title("x[n] * y[n]")
ax[1][0].grid(True)
ax[1][0].set_xlabel("n")
ax[1][0].set_ylabel("Amplitude")

ax[1][1].plot(freq, X_shifted, label='X(f)', color='blue')
ax[1][1].plot(freq, Y_shifted, label='Y(f)', color='green')
ax[1][1].plot(freq, Z_shifted, label='Z(f)', color='orange')
ax[1][1].plot(freq, Z_product_shifted, '*', label='X(f)*Y(f)', color='r')
ax[1][1].set_title("Frequency domain")
ax[1][1].set_xlabel("Frequency (Hz)")
ax[1][1].set_ylabel("Amplitude")
ax[1][1].grid(True)
ax[1][1].legend()

plt.tight_layout()
plt.show()