#!/usr/bin/python3

import sys
import time

import dirmanage


from src.agenda import Agenda
from src.event import Event
_ = dirmanage


def show_event(event: Event):
    """Show the event text."""
    print("=\n" * 5)
    print(event.text, "\n")
    print("=\n" * 5)
    if not event.reccurence:
        return
    ident = event.ident
    script_path = dirmanage.init_dir / "apply_reccursion.py"
    agenda_path = event.agenda.filepath
    command = f"{script_path} {agenda_path} {ident}"
    print(command)


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
