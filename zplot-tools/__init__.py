import shutil
import matplotlib
from pathlib import Path

def register_styles():
    style_dir = Path(matplotlib.get_configdir()) / "stylelib"
    style_dir.mkdir(parents=True, exist_ok=True)

    source_dir = Path(__file__).parent / "mpl_styles"
    for style_file in source_dir.glob("*"):
        target = style_dir / style_file.name
        shutil.copyfile(style_file, target)
