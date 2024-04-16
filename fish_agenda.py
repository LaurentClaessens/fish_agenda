#!/usr/bin/python3

import time
import datetime
from pathlib import Path

import dirmanage
from src.utilities import read_json_file
from src.utilities import write_json_file
_ = dirmanage


dprint = print


def show_event(event):
    """Show the event text."""
    print("=\n" * 5)
    print(event["text"], "\n")
    print("=\n" * 5)


def get_exp_ts(event) -> float:
    """Return the timestamp of the event."""
    json_date = event["date"]
    exp_datetime = datetime.datetime(**json_date)
    base_timestamp = exp_datetime.timestamp()
    exp_ts = base_timestamp

    add_to_date = event.get("add_to_date", {})

    days = add_to_date.get("days", 0)
    exp_ts = exp_ts + 24*3600 * days

    weeks = add_to_date.get("weeks", 0)
    exp_ts = exp_ts + 24*3600*7 * weeks

    return exp_ts


def do_work():
    """Do the work."""
    agenda_file = Path.home() / "agenda.json"
    agenda = read_json_file(agenda_file)
    done_events = False
    ts_to_event: dict[float, dict] = {}
    for event in agenda:
        now = time.time()
        exp_ts = get_exp_ts(event)
        ts_to_event[exp_ts] = event

        if now > exp_ts:
            show_event(event)
            print("nvim ", agenda_file.resolve())
            journal_file = Path.home() / "Documents_sources/journal/journal.md"
            print(f"nvim {journal_file}")
            done_events = True

    if not done_events:
        print("On y va!")

    ts_to_event = dict(sorted(ts_to_event.items()))
    re_events = list(ts_to_event.values())
    write_json_file(re_events, agenda_file, pretty=True)


do_work()
