# Clock module

import string
import struct
from tkinter import NO
from tkinter.messagebox import RETRY
from xml.dom.expatbuilder import theDOMImplementation
from xmlrpc.client import boolean


class Time():
    _the_hour:int
    _the_minute:int
    _the_second:int

    def __init__(self) -> None:
        self._the_hour = 0
        self._the_minute = 0
        self._the_second = 0

class Date():
    _the_year:int
    _the_month:int
    _the_day:int

    def __init__(self) -> None:
        self._the_day = 1
        self._the_month = 1
        self._the_year = 2000

class Clock():
    _the_time:Time
    _the_date:Date
    _state:int

    def __init__(self) -> None:
        self._the_time = Time()
        self._the_date = Date()
        self._state = 1

    def change_mode(self) -> str:
        return None
    
    def ready(self) ->str:
        return None
    
    def set(self, p1:int, p2:int, p3:int)-> string:
        return None
        