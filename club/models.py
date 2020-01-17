from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Meeting(models.Model):
    meetingtitle = models.CharField(max_length=255)
    meetingdate = models.DateField()
    meetingtime = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=255)
    agenda = models.CharField(max_length=255)

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table = 'Meeting'
        verbose_name_plural = 'Meeting'


class Meetingminutes(models.Model):
    meetingid = models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance = models.ManyToManyField(User)
    minutestext = models.CharField(max_length=255)

    def __str__(self):
        return self.minutestext

    class Meta:
        db_table = 'Meetingminutes'
        verbose_name_plural = 'Meetingminutes'


class Resource(models.Model):
    resourcename = models.CharField(max_length=255)
    resourcetype = models.CharField(max_length=255)
    dateentered = models.DateField()
    URL = models.URLField(null=True, blank=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table = 'Resource'
        verbose_name_plural = 'Resource'


class Event(models.Model):
    eventtitle = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    URL = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=255)
    userid = models.DecimalField(max_digits=5, decimal_places=0, null=True, blank=True)

    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table = 'Event'
        verbose_name_plural = 'Event'