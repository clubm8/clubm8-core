from django.db import models


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


class SpecialOccurrence(models.Model):
    date = models.DateField()
    occurence = models.ForeignKey(Occurrence)

    def __str__(self):
        return "{} @ {}".format(self.occurence, self.date)


class Plan(models.Model):
    occurence = models.ForeignKey(Occurrence, null=True)

    def __str__(self):
        return "{}".format(self.occurence)


class Slot(models.Model):
    plan = models.OneToOneField(Plan, null=True)
    start = models.DateField()

    def __str__(self):
        "{} @ {}".format(self.plan, self.start)
