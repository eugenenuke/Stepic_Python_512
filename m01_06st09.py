#!/usr/bin/env python3

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, item):
        super(LoggableList, self).log(item)
        super(LoggableList, self).append(item)

x=LoggableList()
x.append(1)
print(x)
