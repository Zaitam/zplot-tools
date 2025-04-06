import shutil
from pathlib import Path
import matplotlib

def register_styles():
    """Copy all .mplstyle files in the package into matplotlib's stylelib."""
    source_dir = Path(__file__).parent / "mpl_styles"
    target_dir = Path(matplotlib.get_configdir()) / "stylelib"
    target_dir.mkdir(parents=True, exist_ok=True)

    for style_file in source_dir.rglob("*.mplstyle"):
        target_file = target_dir / style_file.name
        shutil.copy(style_file, target_file)
