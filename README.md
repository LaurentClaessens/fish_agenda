# fish agenda

This simple agenda utility prints the events that you have to recall. Your list of events is a json.

## Example.

Here is `agenda.json`:


```
[
  {
    "date": {
      "year": 2025,
      "month": 1,
      "day": 19
    },
    "text": "Supper tonight"
  },
  {
    "date": {
      "year": 2026,
      "month": 3,
      "day": 7,
      "hour": 12
    },
    "text": "This afternoon I do something."
    }
]
```

- If you run `./fish_agenda.py agenda.json` before of January 19 2025, the script does nothing.
- If you run `./fish_agenda.py agenda.json` on January 19 2025 or later, the script prints "Supper tonight".
- If you run `./fish_agenda.py agenda.json` on March 7 2026 at 12h or later, the script prints "This afternoon I do nothing".

## Sort the json file

Run `./sort_agenda.py agenda.json` rewrites the file `agenda.json` sorting the events by date.

## Recall again later

```
{
    "date": {
      "year": 2026,
      "month": 3,
      "day": 7,
      "hour": 12
    },
    "add_to_date":
    {
    "days": 2,
    }
    "text": "Buy milk"
    }
```

This event is planned for March 9 2026 at 12 (March 7 + 2 days). One can add hours, days, weeks, mounts, years.

## Recurring events

If I need to do something every monday, I do as follow
```
{
    "date": {
      "year": 2024,
      "month": 8,
      "day": 19
    },
    "add_to_date":
    {
    "weeks": 3,
    }
    "text": "Do somethin on monday"
    }
```

August 19 2024 is a Monday. Each week I have the recall and I add 1 to the "add weeks" line.

## Done events

```
  {
    "date": {
      "year": 2024,
      "month": 8,
      "day": 12
    },
    "text": "See Mary Sue",
    "done": true
  }
```

Add the line `"done": true` and the event will not be displayed. The events with `done:true` will be sorted at the end of the json file.
