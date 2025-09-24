import matplotlib.pyplot as plt
import numpy as np

# Create a simple plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title("Test Plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.savefig("test_plot.png", dpi=300, bbox_inches='tight')
plt.show()

print("Test plot created successfully!")