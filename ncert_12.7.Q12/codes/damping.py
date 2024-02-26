import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 1  # Resistance in ohms
L = 50e-6  # Inductance in henrys
C = 50e-6  # Capacitance in farads

# Angular frequency and phase angle
angular_freq = 1 / np.sqrt(L * C)
phi = np.arccos(2 / np.sqrt(5))

Q_o = 10e-3/np.cos(phi)

# Time parameters
t_start = 0
t_end = 5e-3
num_points = 1000000                                            

# Time array
time = np.linspace(t_start, t_end, num_points)

# Calculate charge, current, and power
charge = Q_o * np.exp(-R * time / (2 * L)) * np.cos(angular_freq * time - phi)
current = (-Q_o * R / (2 * L)) * np.exp(-R * time / (2 * L)) * np.cos(angular_freq * time - phi) + Q_o*np.exp(-R * time / (2 * L))*np.sin(angular_freq * time - phi)*(-angular_freq)
power = current**2 * R


plt.clf()
# Plotting Charge

plt.plot(time, charge, label='Charge')
plt.xlabel('Time (s)')
plt.ylabel('Charge (Coulombs)')
plt.title('Charge as a function of time')
plt.grid(True)
plt.legend()
plt.savefig("Charge across capacitor during Damping")
plt.clf()


# Plotting Current

plt.plot(time, current, label='Current', color='tab:orange')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.title('Current as a function of time')
plt.grid(True)
plt.legend()
plt.savefig("Current in circuit during damping")
plt.clf()

# for verification
area_under_power_curve = np.trapz(power, time)

print("Area under the power curve:", area_under_power_curve, "Joules")

# Plotting Power

plt.plot(time, power,label=f'Power', color='tab:red')
plt.xlabel('Time (s)')
plt.ylabel('Power (W)')
plt.title('Power as a function of time')
plt.grid(True)
plt.legend()
plt.savefig("Power Dissipated across Resistor")
plt.clf()


