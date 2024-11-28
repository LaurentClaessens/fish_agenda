#!/usr/bin/python3

"""Mark the event as done."""

import sys

from src.agenda import Agenda


def do_work():
    """Do the work."""
    ident = sys.argv[2]
    filename = sys.argv[1]
    agenda = Agenda(filename)
    event = agenda.get_event(ident)
    event.mark_as_done()
    agenda.rewrite_sorted()


do_work()
