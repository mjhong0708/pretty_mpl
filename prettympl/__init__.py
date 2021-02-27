import os
from glob import glob
from prettympl.styles import simple_white
import matplotlib.font_manager as fm

__version__ = "0.0.2"
_current_dir = os.path.dirname(os.path.realpath(__file__))
_font_dir_root = os.path.join(_current_dir, "fonts")


def set_style(style="simple_white", **kwargs):
    """Set style of plot.
    :param style: string. Define style of plot. Currently only supports "simple_white".
    :param kwargs: Some options.
        fontfamily: Font family. Default is 'Arial'. Supported fonts are:
                    ['Arial', 'Helvetica Now Display', 'Helvetica Now Text',
                           'Lato', 'SF Pro Text', 'SF Pro Display', 'Spoqa Han Sans Neo', 'Times New Roman']
        fontsize: float. Size of default font. Size of axes labels are 1.2 * fontsize. Default is 8.
        usetex: bool. If true, texts are rendered with tex. Default is False.
        figsize: tuple. Dimension of figure as units of cm. Default is (8, 6).
        axes_lw: float. Line width of axes frame. Default is 0.9.
        num_minorticks: int. Number of minor ticks. Default is 2.
        lw = Default linewidth for line plot. Default is 0.75.
        ms = Default marker size for marker plot. Default is 3.7.
        mew =Default edge width of marker for marker plot. Default is 0.6.
    """
    if style == "simple_white":
        simple_white(**kwargs)


_available_fonts = []
for font_path in glob(f"{_font_dir_root}/*/*.*tf"):
    font = fm.get_font(font_path)
    _available_fonts.append(font.family_name)
    fm.fontManager.addfont(font_path)
