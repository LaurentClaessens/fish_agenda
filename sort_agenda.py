#!/usr/bin/python3

"""Sort and rewrite the file `agenda.json`."""

import sys

from src.utilities_b import rewrite_sorted
from src.agenda import Agenda


def do_work():
    """Do the work."""
    filename = sys.argv[1]
    agenda = Agenda(filename)
    rewrite_sorted(agenda)


do_work()
