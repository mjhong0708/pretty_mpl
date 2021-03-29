from typing import Tuple
import matplotlib.pyplot as plt
import matplotlib.legend as mlegend


def figsize_cm(figsize: tuple) -> tuple:
    figsize_in_cm = (figsize[0] / 2.54, figsize[1] / 2.54)
    return figsize_in_cm

class Style:
    def __init__(
            self, font_family: str, font_size: float,
            figsize: Tuple[float, float], axes_lw: float,
            legend_lw: float, **kwargs):
        """
        :param font_family: Font family
        :param font_size: Font size
        :param figsize: Figure size
        :param axes_lw: Linewidth of axes frame
        :param legend_lw: Linewidth of legend frame
        """
        self.font_family = font_family
        self.font_size = font_size
        self.figsize = figsize
        self.axes_lw = axes_lw
        self.legend_linewidth = legend_lw

        # Additional arguments
        self.lw = kwargs.get("lw", 0.75)
        self.ms = kwargs.get("ms", 3.7)
        self.mew = kwargs.get("mew", 0.6)
        self.num_minorticks = kwargs.get("num_minorticks", 2)

        # Additional properties : to be multiplied by figure area

    def __enter__(self):
        self.use()

    def use(self):
        # Font setup
        plt.rcParams['font.family'] = self.font_family
        plt.rcParams['font.size'] = self.font_size
        plt.rcParams['mathtext.default'] = 'regular'

        # Figure properties
        plt.rcParams['figure.figsize'] = figsize_cm(self.figsize)
        plt.rcParams['figure.dpi'] = 200

        # Axes properties
        plt.rcParams['axes.linewidth'] = self.axes_lw
        plt.rcParams['axes.labelsize'] = self.font_size * 1.2
        plt.rcParams['axes.titlesize'] = self.font_size * 1.2

        # Lineplot setup
        plt.rcParams['lines.linewidth'] = self.lw
        plt.rcParams['lines.markersize'] = self.ms
        plt.rcParams['lines.markeredgewidth'] = self.mew

    def __exit__(self, exc_type, exc_val, exc_tb):
        fig = plt.gcf()
        for ax in fig.axes:
            handles, _ = mlegend._get_legend_handles_labels([ax])
            if len(handles) != 0:
                legend = ax.get_legend()
                frame = legend.get_frame()
                frame.set_linewidth(self.legend_linewidth)
        plt.rcdefaults()
        plt.tight_layout()
