import matplotlib.pyplot as plt
import numpy as np

#evenly sampled time at 200ms interval
t = np.arange(0., 5., 0.2)

#red dashes, blue squares and green triangle
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
