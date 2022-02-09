# Clock module

import string
import struct
from tkinter import NO
from tkinter.messagebox import RETRY
from xmlrpc.client import boolean


class Time():
    _the_hour:int
    _the_minute:int
    _the_second:int

class Date():
    _the_year:int
    _the_month:int
    _the_day:int

class Clock():
    _the_time:Time
    _the_date:Date
    _state:int

    def __init__(self) -> None:
        self._the_time = None
        self._the_date = None
        self._state = None

    def change_mode(self) -> str:
        return None
    
    def ready(self) ->str:
        return None
    
    def set(self, p1:int, p2:int, p3:int)-> string:
        return None
        