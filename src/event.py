"""A class for an event."""


from typing import Any
from typing import TYPE_CHECKING

from src.utilities_b import get_exp_ts
from src.utilities import random_string

if TYPE_CHECKING:
    from src.agenda import Agenda


class Event:

    def __init__(self, agenda: 'Agenda', j_event: dict[str, Any]):
        """Initialize."""
        self.agenda = agenda
        self.j_event = j_event
        self.exp_ts = get_exp_ts(self.j_event)
        self.text = self.j_event['text']
        self.ident = self.get_ident()
        self.reccurence: dict[str, int] = self.j_event.get("reccurence", {})

    def get_ident(self):
        """Return an ident for the event."""
        if "ident" in self.j_event:
            return self.j_event["ident"]
        ident = random_string(10)
        self.j_event["ident"] = ident
        return ident

    def mark_as_done(self):
        """Pass the 'done' to true."""
        self.j_event["done"] = True

    def apply_reccursion(self):
        """Add to the date the reccursion time."""
        add_to: dict[str, int] = self.j_event.get("add_to_date", {})
        all_keys = list(self.reccurence.keys()) + list(add_to.keys())
        new_add_to: dict[str, int] = {}
        for key in all_keys:
            added = add_to.get(key, 0)
            reccu = self.reccurence.get(key, 0)
            new_add = added + reccu
            if new_add > 0:
                new_add_to[key] = new_add
        self.j_event['add_to_date'] = new_add_to

    def to_json(self):
        """return a json representation of self."""
        return self.j_event
