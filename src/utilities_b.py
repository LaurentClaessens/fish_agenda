"""
Some utilities functions.

This file contains the functions that are specific 
to this project.
"""

import datetime
from typing import TYPE_CHECKING
from dateutil.relativedelta import relativedelta        # type:ignore


from src.utilities import write_json_file

if TYPE_CHECKING:
    from src.agenda import Agenda


def get_exp_ts(event: dict) -> float:
    """Return the timestamp of the event."""
    json_date = event["date"]
    exp_datetime = datetime.datetime(**json_date)
    json_delta = event.get("add_to_date", {})
    delta = relativedelta(**json_delta)
    exp_date = exp_datetime + delta
    return exp_date.timestamp()


def rewrite_sorted(agenda: 'Agenda'):
    """Rewrite the agenda file with sorted events."""
    events = agenda.events
    events.sort(key=lambda x: x.exp_ts)
    j_events = [event.to_json() for event in events]
    write_json_file(j_events, agenda.filepath, pretty=True)
