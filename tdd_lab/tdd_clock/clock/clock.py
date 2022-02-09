# Clock module

import string
import struct
from tkinter import NO
from tkinter.messagebox import RETRY
from xmlrpc.client import boolean


class Time():
    pass

class Date():
    pass

class Clock():
    _the_time:Time
    _the_date:Date
    _state:str

    def __init__(self) -> None:
        self._the_time = None
        self._the_date = None
        self._state = None

    def change_mode(self) -> str:
        return None
    
    def ready(self) ->str:
        return None
    
    def set(p1:int, p2:int, p3:int)-> string:
        return None
        