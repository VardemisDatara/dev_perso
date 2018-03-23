#!/usr/bin/python
import struct
from collection import namedtuple
import pprint 

class datahandler:
    def __init__(self, dataname, datalist):
        self.data = namedtuple(dataname, datalist)
        self.compress = ''
        self.format = ''
        self.size = 0
