#!/usr/bin/python3

import sys
import time

import dirmanage

from src.event import Event
from src.agenda import Agenda
from src.utilities import ColorOutput
_ = dirmanage


def show_event(event: Event):
    """Show the event text."""
    ident = event.ident
    agenda_path = event.agenda.filepath
    with ColorOutput("green"):
        print(event.text)
    if not event.reccurence:
        script_path = dirmanage.base_dir / "mark_as_done.py"
    else:
        script_path = dirmanage.base_dir / "apply_reccursion.py"
    command = f"{script_path} {agenda_path} {ident}"
    print(command)
    print("")


def do_work():
    """Do the work."""
    filename = sys.argv[1]
    agenda = Agenda(filename)

    one_done = False
    for event in agenda:
        now = time.time()

        if now > event.exp_ts:
            show_event(event)
            one_done = True

    if one_done:
        print(f"nvim {agenda.filepath}")
    else:
        print("On y va!")


do_work()
