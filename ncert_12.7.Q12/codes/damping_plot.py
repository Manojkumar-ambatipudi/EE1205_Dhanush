import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.loadtxt('data_for_damping.txt', skiprows=1)


time = data[:, 0]
voltage = data[:, 1]
current = data[:, 2]
power = data[:, 3]

# Plotting Voltage
plt.plot(time, voltage, label='Voltage')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Voltage as a function of time')
plt.grid(True)
plt.legend()
plt.savefig("Voltage_plot.png")
plt.clf()

# Plotting Current
plt.plot(time, current, label='Current', color='tab:orange')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.title('Current as a function of time')
plt.grid(True)
plt.legend()
plt.savefig("Current_plot.png")
plt.clf()

# Plotting Power
plt.plot(time, power, label='Power', color='tab:red')
plt.xlabel('Time (s)')
plt.ylabel('Power (W)')
plt.title('Power as a function of time')
plt.grid(True)
plt.legend()
plt.savefig("Power_plot.png")
plt.clf()
