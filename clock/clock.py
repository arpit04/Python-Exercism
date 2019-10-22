total_minutes = 1440

class Clock(object):
    def __init__(self, hour, minute):
        self.minutes = ((hour * 60) + minute) % total_minutes

    def __repr__(self):
        print(self.minute)
        return '{}:{}'.format(
                str(self.minutes // 60).zfill(2),
                str(self.minutes % 60).zfill(2)
            )

    def __eq__(self, other):
        print("equal minutes")
        return self.minutes == other.minutes

    def __add__(self, minutes):
        print("add minutes")
        return Clock(0, self.minutes + minutes)

    def __sub__(self, minutes):
        print("subtract minutes")
        return Clock(0, self.minutes - minutes)