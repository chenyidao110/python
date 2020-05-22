import time

#define clock class

class Clock(object):
    """clock class"""

    def __init__(self, hour=0, minute=0, second=0):
        """init method
        :param hour
        :param minute
        :param second
        """
        self.hour = hour
        self.min = minute
        self.sec = second

    def run(self):
        """running"""
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            if self.min == 60:
                self.min = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        """show time"""
        return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'

#create clock object
clock = Clock(23,59,58)
while True:
    print(clock.show())
    time.sleep(1)
    clock.run
