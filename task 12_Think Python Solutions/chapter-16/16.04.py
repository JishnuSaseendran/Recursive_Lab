

import sys
import os
from copy import copy

class Time(object):
    hour=0
    minute=0
    seconds=0
def print_time(time_obj):
    hour, minute, second = time_obj.hour, time_obj.minute, time_obj.second
    print ':'.join([str(hour), str(minute), str(second)])


def increment(time_obj, seconds):
    obj = Time()
    obj = copy(time_obj)
    
    obj.second += seconds
    if obj.second >= 60: 
        added_min, remaining_sec = divmod(obj.second, 60)
        obj.second = remaining_sec
        obj.minute += added_min
    if obj.minute >= 60:
        added_hour, remaining_min = divmod(obj.minute, 60)
        obj.minute = remaining_min
        obj.hour += added_hour
    return obj

def main():
    t = Time()
    t.hour = 0 
    t.minute = 0
    t.second = 0
    seconds = int(input("Enter Seconds: "))
    
    print "Initial Time"
    print_time(t)
    print 
    print "New time"
    print_time(increment(t, seconds))
    


if __name__ == '__main__':
    main()
