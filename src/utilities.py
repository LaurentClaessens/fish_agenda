import json
from typing import Any
from pathlib import Path
from typing import Union
from typing import Optional
from colorama import Fore, Back, Style

import random
import string
import contextlib


PathOrStr = Union[Path, str]


class ColorOutput:
    """Colored output"""

    def __init__(self, fg: Optional[str] = None, bg: Optional[str] = None):
        """Initialize."""
        self.fg = fg
        self.bg = bg

    def __exit__(self, *args):
        """Reset all the colors"""
        _ = args
        print(Style.RESET_ALL, end="\r")

    def __enter__(self):
        """Initiate the requested color."""
        fg_correspondance = {
            "black": Fore.BLACK,
            "red": Fore.RED,
            "green": Fore.GREEN,
            "yellow": Fore.YELLOW,
            "blue": Fore.BLUE,
            "magenta": Fore.MAGENTA,
            "cyan": Fore.CYAN,
            "white": Fore.WHITE
        }
        bg_correspondance = {
            "black": Back.BLACK,
            "red": Back.RED,
            "green": Back.GREEN,
            "yellow": Back.YELLOW,
            "blue": Back.BLUE,
            "magenta": Back.MAGENTA,
            "cyan": Back.CYAN,
            "white": Back.WHITE}

        if self.fg:
            print(fg_correspondance[self.fg], end="\r")
        if self.bg:
            print(bg_correspondance[self.bg], end="\r")

    def __call__(self, fun):
        """Turn the color outpus to a context manager"""
        def wrapper(*args, **kwargs):
            """Wrap the function."""
            with self:
                return fun(*args, **kwargs)
        return wrapper


def random_string(length):
    """Return a random string of letters of the given length."""
    rn_list = [random.choice(string.ascii_letters) for _ in range(1, length)]
    return "".join(rn_list)


def read_json_file(json_path: PathOrStr, default=None):
    """Return the given json file as dictionary."""
    json_path = Path(json_path)
    if not json_path.is_file():
        if default is None:
            raise ValueError(f"You try to read {json_path}. "
                             f"The file does not exist and you "
                             f"furnished no default.")
        return default
    with open(json_path, 'r') as json_data:
        try:
            answer = json.load(json_data)
        except json.decoder.JSONDecodeError as err:
            print("JSONDecodeError:", err)
            message = f"Json error in {json_path}:\n {err}"
            raise ValueError(message) from err
    return answer


def json_serial(obj):
    """Serialize the datetime."""
    with contextlib.suppress(AttributeError):
        return obj.to_json()
    if isinstance(obj, Path):
        return str(obj)
    if isinstance(obj, set):
        return list(obj)
    return str(obj)


def json_to_str(json_dict, pretty=False, ensure_ascii=True):
    """Return a string representation of the given json."""
    if pretty:
        return json.dumps(json_dict,
                          indent=4,
                          default=json_serial,
                          ensure_ascii=False)
    return json.dumps(json_dict, default=json_serial, ensure_ascii=ensure_ascii)


def print_json(json_obj: Any):
    """Print the given json."""
    my_str = json_to_str(json_obj, pretty=True)
    print(my_str)


def write_json_file(json_dict,
                    filename: PathOrStr,
                    pretty=False,
                    parents=False):
    """Write the dictionary in the given file."""
    filename = Path(filename)
    if parents:
        parent = filename.parent
        parent.mkdir(parents=True, exist_ok=True)
    my_str = json_to_str(json_dict, pretty=pretty)

    filename.write_text(my_str)
