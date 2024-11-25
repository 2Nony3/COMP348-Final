import matplotlib.pyplot as plt
import numpy as np

# Generate data for the cardioid
theta = np.linspace(0, 2 * np.pi, 1000)
r = 1 - np.sin(theta)

# Convert polar coordinates to Cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot the cardioid
plt.plot(x, y, label='Cardioid')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Cardioid Plot')

# Add a legend
plt.legend()

# Display the plot
plt.axis('equal')  # Ensure equal scaling for x and y axes
plt.show()