#!/usr/bin/python3

"""Add some weeks/days to the event."""

import sys

from src.agenda import Agenda


def do_work():
    """Do the work."""
    ident = sys.argv[2]
    filename = sys.argv[1]
    agenda = Agenda(filename)
    event = agenda.get_event(ident)
    event.apply_reccursion()
    agenda.rewrite_sorted()


do_work()
