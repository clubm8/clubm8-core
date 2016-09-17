from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timedelta


class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=128)
    tag = models.ManyToManyField(Tag)
    location = models.CharField(max_length=128)

    def __str__(self):
        return "{} @ {}".format(self.name, self.location)


class Occurrence(models.Model):
    weekday = models.IntegerField()
    start = models.TimeField()
    duration = models.IntegerField()
    event = models.ForeignKey(Event)

    def __str__(self):
        return "{} # {}".format(self.event, self.start)

    def weekday_str(self):
        return ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][self.weekday]

class SpecialOccurrence(models.Model):
    date = models.DateField()
    occurence = models.ForeignKey(Occurrence)

    def __str__(self):
        return "{} @ {}".format(self.occurence, self.date)


class Plan(models.Model):
    name = models.CharField(max_length=128, null=True)
    occurence = models.ManyToManyField(Occurrence)

    def __str__(self):
        return "{}".format(self.name)


class Slot(models.Model):
    plan = models.ForeignKey(Plan, null=True)
    start = models.DateField()

    def __str__(self):
        return "{} @ {}".format(self.plan, self.start)

    def special_events(self):
        return SpecialOccurrence.objects.filter(date__range=[self.start, self.start + timedelta(days=6)])


class News(models.Model):
    author = models.ForeignKey(User)
    date = models.DateField()
    time = models.TimeField()
    title = models.CharField(max_length=128)
    text = models.TextField()

    class Meta:
        verbose_name_plural='News'

    def __str__(self):
        return "'{}' by {} on {}".format(self.title, self.author, self.date)
