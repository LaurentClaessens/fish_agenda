#!venv/bin/python3


import sys
import datetime

import tkinter as tk
from tkcalendar import DateEntry

from src.agenda import Agenda


class UserDateChooser:
    """
    Show a calendar date picker.

    Usage:
    UserDateChooser().get_date()

    A calendar is presented, the user select the date and
    the datetime.datetime is returned.
    (the tk loop is also exited)
    """

    def __init__(self):
        """Create the tk objects but do not show them."""
        self.root = tk.Tk()
        self.cal = DateEntry(self.root,
                             width=12,
                             background='darkblue',
                             foreground='white',
                             borderwidth=2)

        self.button = tk.Button(self.root,
                                text="Get Date",
                                command=self._grab_date)
        self.selected: datetime.datetime

    def _grab_date(self):
        """Grab the date and exit the tk pannel."""
        selected: datetime.datetime = self.cal.get_date()
        self.selected = selected
        self.root.destroy()

    def get_date(self):
        """Return the selected date."""
        self.button.pack(pady=20)
        self.cal.pack(padx=10, pady=10)
        self.root.mainloop()
        return self.selected


def do_work():
    filename = sys.argv[1]
    agenda = Agenda(filename)
    sel_date = UserDateChooser().get_date()
    year = sel_date.year
    month = sel_date.month
    day = sel_date.day
    print(year, month, day)

    text = input("Your text: ")
    print(text)

    agenda.add_envent(sel_date, text)
    agenda.rewrite_sorted()


do_work()
