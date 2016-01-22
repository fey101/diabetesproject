import datetime

from django.db import models
from django.utils import timezone


class UserCalendar(models.Model):
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField()

    def is_morning(self):
        midnight = datetime.timedelta(0)
        midday = datetime.timedelta(hours=12)
        if self.start > midnight and self.end < midday:
            return True
        else:
            return False

    def is_lunch(self):
        midday = datetime.timedelta(hours=12)
        if (self.start >= midday) and (
                self.end < midday + datetime.timedelta(hours=2)):
                    return True
        else:
            return False

    def is_afternoon(self):
        midday = datetime.timedelta(hours=12)
        if (self.start >= midday) and (
                self.end < midday + datetime.timedelta(hours=4)):
                    return True
        else:
            return False

    def is_evening(self):
        midday = datetime.timedelta(hours=12)
        if (self.start >= midday + datetime.timedelta(4)) and (
                self.end < midday + datetime.timedelta(hours=7)):
                    return True
        else:
            return False

    def is_nighttime(self):
        midnight = datetime.timedelta()
        if (self.start >= midnight - datetime.timedelta(hours=5)) and (
                self.end <= midnight - datetime.timedelta(minutes=1)):
                    return True
        else:
            return False
