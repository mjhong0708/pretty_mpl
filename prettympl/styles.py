import matplotlib as mpl
from cycler import cycler
from matplotlib import font_manager as fm
import matplotlib.ticker


def simple_white(
        fontfamily: str = 'Arial',
        fontsize: float = 8,
        usetex: bool = False,
        figsize: tuple = (8, 6),
        axes_lw: float = 0.9,
        num_minorticks: int = 2,
        **kwargs

):
    lw = kwargs.get("lw", 0.75)
    ms = kwargs.get("ms", 3.7)
    mew = kwargs.get("mew", 0.6)

    # General font settings
    mpl.rcParams['font.family'] = fontfamily
    mpl.rcParams['font.size'] = fontsize
    mpl.rcParams['mathtext.default'] = 'regular'
    mpl.rcParams['text.usetex'] = usetex

    # Color cycler settings
    mpl.rcParams['axes.prop_cycle'] = cycler(color=[
        "black", "mediumblue", "darkgreen", "firebrick", "mediumvioletred"]
    )

    # Figure properties
    mpl.rcParams['figure.figsize'] = (figsize[0] / 2.54, figsize[1] / 2.54)
    mpl.rcParams['figure.dpi'] = 200

    # Axes properties
    mpl.rcParams['axes.linewidth'] = axes_lw
    mpl.rcParams['axes.labelsize'] = fontsize * 1.2
    mpl.rcParams['axes.titlesize'] = fontsize * 1.2

    # Ticks properties
    class MyLocator(matplotlib.ticker.AutoMinorLocator):
        def __init__(self, n=num_minorticks):
            super().__init__(n=n)

    matplotlib.ticker.AutoMinorLocator = MyLocator
    mpl.rcParams["xtick.minor.visible"] = True
    mpl.rcParams["ytick.minor.visible"] = True
    mpl.rcParams["xtick.direction"] = 'in'
    mpl.rcParams['xtick.major.size'] = 2.5
    mpl.rcParams['xtick.major.width'] = axes_lw
    mpl.rcParams['xtick.minor.size'] = 1.4
    mpl.rcParams['xtick.minor.width'] = axes_lw
    mpl.rcParams["ytick.direction"] = 'in'
    mpl.rcParams['ytick.major.size'] = 2.5
    mpl.rcParams['ytick.major.width'] = axes_lw
    mpl.rcParams['ytick.minor.size'] = 1.4
    mpl.rcParams['ytick.minor.width'] = axes_lw

    # Legend properties
    mpl.rcParams['legend.framealpha'] = 1
    mpl.rcParams['legend.edgecolor'] = 'k'
    mpl.rcParams['legend.fancybox'] = False
    mpl.rcParams['legend.fontsize'] = fontsize

    # plot setting
    mpl.rcParams['lines.linewidth'] = lw
    mpl.rcParams['lines.markersize'] = ms
    mpl.rcParams['lines.markeredgewidth'] = mew
