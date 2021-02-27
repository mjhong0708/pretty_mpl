import os
import pickle
from glob import glob
from prettympl.styles import simple_white
import matplotlib.font_manager as fm

__version__ = "0.0.1"
_current_dir = os.path.dirname(os.path.realpath(__file__))
_font_dir_root = os.path.join(_current_dir, "fonts")


def set_style(style="simple_white", **kwargs):
    if style == "simple_white":
        simple_white(**kwargs)


_available_fonts = []
for font_path in glob(f"{_font_dir_root}/*/*.*tf"):
    font = fm.get_font(font_path)
    _available_fonts.append(font.family_name)
    fm.fontManager.addfont(font_path)
