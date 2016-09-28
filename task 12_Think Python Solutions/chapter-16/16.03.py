
import sys
import os


class Time(object):
    hour=0
    minut=0
    second=0

def print_time(time_obj):
    hour, minute, second = time_obj.hour, time_obj.minute, time_obj.second
    print ':'.join([str(hour), str(minute), str(second)])

def increment(time, seconds): 
    time.second += seconds
    if time.second >= 60: 
        added_min, remaining_sec = divmod(time.second, 60)
        time.second = remaining_sec
        time.minute += added_min
    if time.minute >= 60:
        added_hour, remaining_min = divmod(time.minute, 60)
        time.minute = remaining_min
        time.hour += added_hour
    

def main():
    t = Time()
    t.hour = 12
    t.minute = 59
    t.second = 30
    
    print "current time"
    print_time(t)
    increment(t, 600)
    print "Time after 600 seconds"
    print_time(t)


if __name__ == '__main__':
    main()
