import time
from datetime import datetime


class Time(object):
    hour=0
    minut=0
    second=0


def days_until_birthday(birthday):
    today = datetime.today()
    next_birthday = datetime(today.year, birthday.month, birthday.day)

    if today > next_birthday:
        next_birthday = datetime(today.year+1, birthday.month, birthday.day)
    delta = next_birthday - today
    return delta.days


def double_day(b1, b2):

    assert b1 > b2
    delta = b1 - b2
    double_day = b1 + delta
    return double_day

def main():
    print "Today is " + time.strftime("%c")
    birthday = datetime(1991, 1, 11)
    print 'Days until birthday',
    print days_until_birthday(birthday)

    b1 = datetime(2006, 12, 26)
    b2 = datetime(2003, 10, 11)
    print 'Double Day',
    print double_day(b1, b2)



if __name__ == '__main__':
    main()
