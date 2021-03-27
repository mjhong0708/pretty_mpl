from abc import ABC
from typing import Tuple

import matplotlib.pyplot as plt
from cycler import cycler
import matplotlib.ticker

from .style import Style


class SimpleWhite(Style):
    def __init__(self, font_family: str = "Arial", font_size: float = 8, figsize=(8,6),
                 axes_lw: float = 0.9, legend_lw: float = 0.45, **kwargs):
        super().__init__(font_family, font_size, figsize, axes_lw, legend_lw, **kwargs)

    def use(self):
        super().use()
        # Color cycler settings
        plt.rcParams['axes.prop_cycle'] = cycler(color=[
            "black", "mediumblue", "darkgreen", "firebrick", "mediumvioletred"]
        )

        # Ticks setup
        class MyLocator(matplotlib.ticker.AutoMinorLocator, ABC):
            def __init__(self, n=self.num_minorticks):
                super().__init__(n=n)

        matplotlib.ticker.AutoMinorLocator = MyLocator
        plt.rcParams["xtick.minor.visible"] = True
        plt.rcParams["ytick.minor.visible"] = True
        plt.rcParams["xtick.direction"] = 'in'
        plt.rcParams['xtick.major.size'] = 2.5
        plt.rcParams['xtick.major.width'] = self.axes_lw
        plt.rcParams['xtick.minor.size'] = 1.4
        plt.rcParams['xtick.minor.width'] = self.axes_lw
        plt.rcParams["ytick.direction"] = 'in'
        plt.rcParams['ytick.major.size'] = 2.5
        plt.rcParams['ytick.major.width'] = self.axes_lw
        plt.rcParams['ytick.minor.size'] = 1.4
        plt.rcParams['ytick.minor.width'] = self.axes_lw

        # Legend setup
        plt.rcParams['legend.fancybox'] = False
        plt.rcParams['legend.fontsize'] = self.font_size
        plt.rcParams['legend.framealpha'] = 1
        plt.rcParams['legend.edgecolor'] = 'k'
        plt.rcParams['legend.facecolor'] = 'none'
