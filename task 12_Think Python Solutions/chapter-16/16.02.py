
import sys
import os


class Time(object):
    hour=0
    minut=0
    second=0

def compute_scalar_time(time_obj):
    return time_obj.hour + (time_obj.minute / 60) + (time_obj.second / 3600)


def is_after(time_obj_1, time_obj_2):
    hour_1, minute_1, second_1 = time_obj_1.hour, time_obj_1.minute, time_obj_1.second
    hour_2, minute_2, second_2 = time_obj_2.hour, time_obj_2.minute, time_obj_2.second
    return compute_scalar_time(time_obj_1) < compute_scalar_time(time_obj_2)


def main():
    t1 = Time()
    t1.hour = 12
    t1.minute = 59
    t1.second = 30

    t2 = Time()
    t2.hour = 11
    t2.minute = 59
    t2.second = 30    
    print is_after(t1, t2)

if __name__ == '__main__':
    main()
