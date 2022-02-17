# Clock module

class Time():
    _the_hour:int
    _the_minute:int
    _the_second:int

    def __init__(self) -> None:
        self._the_hour = 0
        self._the_minute = 0
        self._the_second = 0
    
    def show_time(self) -> str:
        return f"{self._the_hour:02}:{self._the_minute:02}:{self._the_second:02}"

    def set_time(self, hour:int, min:int, sec:int) -> str:
        if (hour > 23) or (hour < 0):
            raise ValueError(f'Hour: {hour} out of range, expected range 0-23')
        self._the_hour = hour
        if (min > 59) or (min < 0):
            raise ValueError(f'Minute: {min} out of range, expected range 0-59')
        self._the_minute = min
        if (sec > 59) or (sec < 0):
            raise ValueError(f'Second: {sec} out of range, expected range 0-59')
        self._the_second = sec

class Date():
    _the_year:int
    _the_month:int
    _the_day:int

    def __init__(self) -> None:
        self._the_day = 1
        self._the_month = 1
        self._the_year = 2000

    def show_date(self) -> str:
        return f"{self._the_day}/{self._the_month}/{self._the_year}"

class Clock():
    _the_time:Time
    _the_date:Date
    _state:int

    def __init__(self) -> None:
        self._the_time = Time()
        self._the_date = Date()
        self._state = 1

    def change_mode(self) -> str:
        if self._state == 1:
            self._state = 2
        elif self._state == 2:
            self._state = 1
        return f'{self._the_time.show_time()} {self._the_date.show_date()}'
    
    def ready(self) -> str:
        if self._state == 1:
            self._state = 3
            output = self._the_time.show_time()
        if self._state == 2:
            self._state = 4
            output = self._the_date.show_date()
        return output
    
    def set(self, p1:int, p2:int, p3:int)-> str:
        if self._state == 1:
            raise ValueError('Can\'t set time in in time mode, ready first.')
        elif self._state == 2:
            raise ValueError('Can\'t set date in in date mode, ready first.')
        elif self._state == 3:
            self._the_time.set_time(p1, p2, p3)
            self._state = 1
            _display = self._the_time.show_time()
        return _display