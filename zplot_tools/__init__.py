import os
import matplotlib.pyplot as plt
import zplot_tools
from .register_styles import read_styles_in_folders

scienceplots_path = zplot_tools.__path__[0]
styles_path = os.path.join(scienceplots_path, "mpl_styles")
stylesheets = read_styles_in_folders(styles_path)

plt.style.core.update_nested_dict(plt.style.library, stylesheets)
plt.style.core.available[:] = sorted(plt.style.library.keys())