"""A class for the agenda."""


from pathlib import Path
import datetime


from src.utilities import read_json_file
from src.utilities import write_json_file
from src.event import Event


class Agenda:

    def __init__(self, filename: str):

        self.filepath = Path(filename).resolve()
        self.events = self._get_events()

    def _get_events(self):
        """Return the list of events."""
        j_agenda = read_json_file(self.filepath)
        return [Event(self, j_event) for j_event in j_agenda]

    def add_envent(self, date: datetime.datetime, text: str):
        """Add an event to the agenda."""
        j_event = {
            "date": {
                "year": date.year,
                "month": date.month,
                "day": date.day,
                "hour": 0
            },
            "add_to_date": {
                "years": 0,
                "months": 0,
                "days": 0,
                "weeks": 0
            },
            "text": text,
            "done": False
        }
        event = Event(self, j_event)
        self.events.append(event)

    def rewrite_sorted(self):
        """Rewrite the file."""
        events = self.events
        events.sort(key=lambda x: x.exp_ts)
        j_events = [event.to_json() for event in events]
        write_json_file(j_events, self.filepath, pretty=True)

    def get_event(self, ident: str) -> Event:
        """Return the event with given ident."""
        for event in self.events:
            if event.ident == ident:
                return event
        raise NameError(f"No event with ident: {ident}")

    def __getitem__(self, index: int):
        return self.events[index]
