import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

q_x1, q_y1 = 0, 0
q_x2, q_y2 = -1, 1

dx1 = X - q_x1
dy1 = Y - q_y1
dx2 = X - q_x2
dy2 = Y - q_y2

r1 = np.sqrt(dx1**2 + dy1**2)
r2 = np.sqrt(dx2**2 + dy2**2)

r1[r1 == 0] = 1e-10
r2[r2 == 0] = 1e-10

Ex1 = dx1/r1**3
Ey1 = dy1/r1**3
Ex2 = -dx2/r2**3
Ey2 = -dy2/r2**3

Ex_total = Ex1 + Ex2
Ey_total = Ey1 + Ey2

plt.streamplot(X, Y, Ex_total, Ey_total, color = 'blue', density = 1.5)
plt.scatter(q_x1, q_y1, color = 'green', s = 50, label = 'Positive Charge')
plt.scatter(q_x2, q_y2, color = 'red', s = 50, label = 'Negative Charge')
plt.grid(True)
plt.legend()
plt.savefig('Electricfield.png')
plt.show()