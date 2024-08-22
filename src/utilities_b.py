"""
Some utilities functions.

This file contains the functions that are specific 
to this project.
"""

import datetime
from dateutil.relativedelta import relativedelta        # type:ignore


def get_exp_ts(event: dict) -> float:
    """Return the timestamp of the event."""
    json_date = event["date"]
    exp_datetime = datetime.datetime(**json_date)
    json_delta = event.get("add_to_date", {})
    delta = relativedelta(**json_delta)
    exp_date = exp_datetime + delta

    if event.get("done", False):
        # Never show the events that are done, and sort them
        # on the bottom of the list
        exp_date += datetime.timedelta(weeks=1000)

    return exp_date.timestamp()
