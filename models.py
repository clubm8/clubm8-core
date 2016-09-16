from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=128)

class Event(models.Model):
    name     = models.CharField(max_length=128)
    tag      = models.ManyToManyField(Tag)
    location = models.CharField(max_length=128)

class Occurrence(models.Model):
    weekday  = models.IntegerField()
    start    = models.TimeField()
    duration = models.IntegerField()
    event    = models.ForeignKey(Event)

class SpecialOccurrence(models.Model):
    date      = models.DateField()
    occurence = models.ForeignKey(Occurrence)

class Plan(models.Model):
    occurence = models.ForeignKey(Occurrence, null=True)

class Slot(models.Model):
    plan  = models.OneToOneField(Plan, null=True)
    start = models.DateField()

