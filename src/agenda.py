"""A class for the agenda."""


from pathlib import Path

from src.utilities import read_json_file
from src.event import Event


class Agenda:

    def __init__(self, filename: str):

        self.filepath = Path(filename).resolve()
        self.events = self._get_events()

    def _get_events(self):
        """Return the list of events."""
        j_agenda = read_json_file(self.filepath)
        return [Event(j_event) for j_event in j_agenda]

    def __getitem__(self, index: int):
        return self.events[index]
