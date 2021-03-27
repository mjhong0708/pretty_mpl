import numpy as np
import matplotlib.pyplot as plt
from prettympl import SimpleWhite


x = np.linspace(-1.3, 1.3, 100)
y1 = x ** 2
y2 = x ** 3

if __name__ == '__main__':
    import numpy as np

    x1 = np.linspace(0, np.pi / 2, 200)
    x2 = np.random.uniform(0, np.pi / 2, 30)
    y1 = np.cos(x1)
    y2 = np.sin(x1)
    y3 = np.random.uniform(-1, 1, 30)
    y4 = np.random.uniform(-1, 1, 30)

    with SimpleWhite(font_family="Stix two text", figsize=(14, 6)) as s:
        plt.figure()
        plt.subplot(121)
        plt.title("title")
        plt.xlabel("xlabel")
        plt.ylabel("ylabel")
        plt.plot(x1, y1, label='cos')
        plt.plot(x1, y2, '--', label='sin')
        plt.plot(x2, y3, 'o', label='scatter1')
        plt.plot(x2, y4, 's', mfc='none', label='scatter2')
        plt.xticks(np.arange(0,1.75,0.25))
        plt.xlim(0,1.5)
        plt.ylim(-3.5, 1.5)
        plt.legend()
        plt.subplot(122)
        plt.title("title")
        plt.xlabel("xlabel")
        plt.ylabel("ylabel")
        plt.plot(x1, y1, label='cos')
        plt.plot(x1, y2, '--', label='sin')
        plt.xticks(np.arange(0, 1.75, 0.25))
        plt.xlim(0, 1.5)
        plt.ylim(-3.5, 1.5)
        plt.legend()

    plt.savefig("prettympl.jpg", dpi=600)
    plt.show()


