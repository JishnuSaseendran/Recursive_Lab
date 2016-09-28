
import sys
import os
from copy import copy

class Time(object):
    hour=0
    minute=0
    seconds=0
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


        
def increment(time, seconds):
    time_seconds = time_to_int(time)
    total_seconds = time_seconds + seconds
    return int_to_time(total_seconds)


def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2) 
    return int_to_time(seconds)


def main():
    t1 = Time()
    t1.hour = 12
    t1.minute = 49
    t1.second = 30

    t2 = Time()
    t2.hour = 1
    t2.minute = 10
    t2.second = 30    
    
    print "Current time"
    print_time(t1)
    print "time to add is"
    print_time(t2)
    s = int(input("Enter Seconds: "))
    print 'Time after %d seconds'%(s)
    print_time(increment(t1, s))
    print "ti +t2 is"
    print_time(add_time(t1, t2))


if __name__ == '__main__':
    main()
