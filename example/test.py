import numpy as np
import matplotlib.pyplot as plt
from prettympl import set_style


x = np.linspace(-1.3, 1.3, 100)
y1 = x ** 2
y2 = x ** 3

set_style(fontfamily="Helvetica Now Display", fontsize=8)
plt.rc('font', weight='medium')
plt.rc('axes', labelweight='medium')
plt.figure()
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.plot(x, y1, label=r'$x^2$')
plt.plot(x[::2], y2[::2], 'o', mfc='none', label=r'$x^3$')
plt.legend(edgecolor='none')
plt.tight_layout()
plt.savefig("test.png", dpi=600)
plt.show()