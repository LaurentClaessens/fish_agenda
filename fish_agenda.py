#!/usr/bin/python3

import time
import datetime
from pathlib import Path

import dirmanage
from src.utilities import read_json_file
_ = dirmanage


dprint = print


def show_event(event):
    """Show the event text."""
    print("=\n" * 5)
    print(event["text"], "\n")
    print("=\n" * 5)


def do_work():
    """Do the work."""
    agenda_file = Path.home() / "agenda.json"
    agenda = read_json_file(agenda_file)
    done_events = False
    for event in agenda:
        json_date = event["date"]
        exp_datetime = datetime.datetime(**json_date)
        exp_timestamp = exp_datetime.timestamp()
        now = time.time()

        if now > exp_timestamp:
            show_event(event)
            print("nvim ", agenda_file.resolve())
            journal_file = Path.home() / "Documents_sources/journal/journal.md"
            print(f"nvim {journal_file}")
            done_events = True

    if not done_events:
        print("On y va!")


do_work()
