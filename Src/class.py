#!/usr/bin/python
import struct
from collections import namedtuple
import pprint 

class datahandler:
    def __init__(self, dataname, datalist):
        self.data = namedtuple(dataname, datalist)
        self.compress = ''
        self.format = ''
        self.size = 0
    def dataformatsize(self):
        return struct.calcsize(self.format)