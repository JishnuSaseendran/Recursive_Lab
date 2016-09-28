class Time(object):
    hour=0
    minute=0
    second=0
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
def main():
  time=Time()
  time.hour=1
  time.minut=31
  time.second=13
  sec=Time.time_to_int(time)
  print(sec)

if __name__=='__main__':
  main()
