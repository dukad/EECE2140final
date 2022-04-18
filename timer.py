import datetime


class Timer():
    def __init__(self):
        self.starttime = datetime.datetime.now()

    def time(self):
        return datetime.datetime.now() - self.starttime

    def reset(self):
        self.starttime = datetime.datetime.now()

    def time_in_secs(self):
        stringtime = str(self.time())
        # print(stringtime)
        mins = int(stringtime[2:4])
        secs = int(stringtime[5:7])
        hrs = int(stringtime[0:1])
        secondspassed = 60*mins + 3600*hrs + secs
        return secondspassed


