"""Manage the subdirectory issue."""


import os
import sys
from pathlib import Path

init_dir = Path(os.getcwd()).resolve()  # pylint: disable=invalid-name
base_dir = Path(sys.argv[0]).parent
sys.path.append(str(base_dir))
