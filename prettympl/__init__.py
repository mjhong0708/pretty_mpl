import os
from glob import glob
import matplotlib.font_manager as fm
from prettympl.styles import SimpleWhite


__version__ = "0.1.0"
_current_dir = os.path.dirname(os.path.realpath(__file__))
_font_dir_root = os.path.join(_current_dir, "fonts")

_available_fonts = []
for font_path in glob(f"{_font_dir_root}/*/*.*tf"):
    font = fm.get_font(font_path)
    _available_fonts.append(font.family_name)
    fm.fontManager.addfont(font_path)
