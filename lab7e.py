#!/usr/bin/env python3
# Student ID: bturjanandinidia

class Time:
    """Simple object type for time of the day.
       Data attributes: hour, minute, second
       Function attributes: __init__, format_time, sum_times, 
                            change_time, time_to_sec, valid_time, __str__, __repr__
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for Time object."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        """Return time object as a formatted string."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two Time objects and return their sum."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Adjust the Time object by a given number of seconds."""
        total_seconds = self.time_to_sec() + seconds
        new_time = sec_to_time(total_seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second

    def time_to_sec(self):
        """Convert a Time object to seconds."""
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self):
        """Check for the validity of the Time object attributes."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.hour >= 24 or self.minute >= 60 or self.second >= 60:
            return False
        return True

    def __str__(self):
        """Return a string representation of the Time object."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return a debug string representation of the Time object."""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

def sec_to_time(seconds):
    """Convert a number of seconds to a Time object."""
    t = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)
    return t

