"""Manage the subdirectory issue."""


import os
import sys
from pathlib import Path

base_dir = Path(__file__).parent.resolve()
init_dir = Path(os.getcwd()).resolve()  # pylint: disable=invalid-name
sys.path.append(str(base_dir))
