import sys
import os


class Time(object):
   hour=0
   minut=0
   second=0

def print_time(time_obj):
    hour, minute, second = time_obj.hour, time_obj.minute, time_obj.second
    print ':'.join([str(hour), str(minute), str(second)])
    
def main():
    time = Time()
    time.hour = 12
    time.minute = 06
    time.second = 11
    print_time(time)

if __name__ == '__main__':
    main()

