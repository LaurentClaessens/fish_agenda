#!/usr/bin/python3

import time
import datetime
from pathlib import Path
from dateutil.relativedelta import relativedelta        # type:ignore

import dirmanage
from src.utilities import read_json_file
from src.utilities import write_json_file
_ = dirmanage


def show_event(event):
    """Show the event text."""
    print("=\n" * 5)
    print(event["text"], "\n")
    print("=\n" * 5)


def get_exp_ts(event) -> float:
    """Return the timestamp of the event."""
    json_date = event["date"]
    exp_datetime = datetime.datetime(**json_date)
    json_delta = event.get("add_to_date", {})
    delta = relativedelta(**json_delta)
    exp_date = exp_datetime + delta
    return exp_date.timestamp()


def rewrite_sorted(ts_to_event: dict[float, dict], agenda_file: Path):
    """Rewrite the agenda file with sorted events."""
    ts_to_event = dict(sorted(ts_to_event.items()))
    re_events = list(ts_to_event.values())
    write_json_file(re_events, agenda_file, pretty=True)


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

    # rewrite_sorted(ts_to_event, agenda_file)


do_work()
