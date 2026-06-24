import numpy as np
import sympy as smp
import matplotlib.pyplot as plt

k = 0.2 
m = 1 
u, t = smp.symbols('u t')
g = 9.8
v = smp.Function('v')
eq = smp.Eq(v(t).diff(t), g - (k/m)*v(t))
sol = smp.dsolve(eq, v(t), ics = {v(0): u})

velocity_expr = sol.rhs
S = smp.integrate(velocity_expr, (t)) - smp.integrate(velocity_expr.subs(t, 0), (t))

S_eq = smp.lambdify((u, t), S)
t_points = np.linspace(0, 10, 20)
s_points = S_eq(10, t_points)

plt.figure(figsize = (11, 7))
plt.plot(t_points, s_points, 'o--', ms = 4.0, lw = 1.5)
plt.minorticks_on()
plt.locator_params(axis = 'x', nbins = 25)
plt.locator_params(axis = 'y', nbins = 20)
plt.xlabel('Time (in s)')
plt.ylabel('Displacement (in m)')
plt.title('Displacement over Time (including Linear Drag)')
plt.grid(which = 'major', color = 'black', linewidth = 1.0)
plt.grid(which = 'minor', color = 'gray', linewidth = 0.5, linestyle = ':')
plt.savefig('LinearDrag.png')
plt.show()