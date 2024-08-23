#!/usr/bin/python3

"""Sort and rewrite the file `agenda.json`."""

import sys

from src.agenda import Agenda


def do_work():
    """Do the work."""
    filename = sys.argv[1]
    agenda = Agenda(filename)
    agenda.rewrite_sorted()


do_work()
