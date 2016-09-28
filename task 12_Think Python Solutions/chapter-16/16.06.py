

import sys
import os
from copy import copy

class Time(object):
    """Represents the time of day.

        attributes: hour, minute, second
    """

def print_time(time_obj):
    hour, minute, second = time_obj.hour, time_obj.minute, time_obj.second
    print ':'.join([str(hour).zfill(2), str(minute).zfill(2), str(second).zfill(2)])


def time_to_int(time):
    minutes = time.hour * 60 + time.minute 
    seconds = minutes * 60 + time.second 
    return seconds


def int_to_time(seconds): 
    time = Time()
    minutes, time.second = divmod(seconds, 60) 
    time.hour, time.minute = divmod(minutes, 60) 
    return time

def mul_time(time, number):
    time_sec = time_to_int(time)
    product = time_sec * number
    return int_to_time(product)

def time_per_mile(time, distance):
    time_obj = time_to_int(time)
    sec_per_mile = time_obj / distance
    return int_to_time(sec_per_mile)



def main():
    t1 = Time()
    t1.hour = 1
    t1.minute = 34
    t1.second = 23

    
    print "Current Time"
    print_time(t1)
    print "New time"
    print_time(mul_time(t1, 10))
    print "Time / distance foolishness"
    t2 = Time()
    t2.hour = 5
    t2.minute = 13
    t2.second = 30
    distance = 5
    print_time(time_per_mile(t2, distance))


if __name__ == '__main__':
    main()
