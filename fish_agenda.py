#!/usr/bin/python3

import sys
import time

import dirmanage

from dateutil.relativedelta import relativedelta        # type:ignore

from src.agenda import Agenda
_ = dirmanage


def show_event(event):
    """Show the event text."""
    print("=\n" * 5)
    print(event.text, "\n")
    print("=\n" * 5)


def do_work():
    """Do the work."""
    filename = sys.argv[1]
    agenda = Agenda(filename)

    one_done = False
    for event in agenda:
        now = time.time()

        if now > event.exp_ts:
            show_event(event)
            print(f"nvim {agenda.filepath}")
            one_done = True

    if not one_done:
        print("On y va!")


do_work()
