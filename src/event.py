"""A class for an event."""


from typing import Any

from src.utilities_b import get_exp_ts


class Event:

    def __init__(self, j_event: dict[str, Any]):
        """Initialize."""
        self.j_event = j_event
        self.exp_ts = get_exp_ts(self.j_event)
        self.text = self.j_event['text']

    def to_json(self):
        """return a json representation of self."""
        return self.j_event
