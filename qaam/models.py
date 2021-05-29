from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Job(models.Model):

    jobID = models.UUIDField(primary_key=True)
    organisation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    division = models.CharField(max_length=50)
    project = models.CharField(max_length=50)
    prefix = models.CharField(max_length=50)
    title = models.CharField(max_length=240)
    narration = models.TextField
    completion = models.BooleanField
    addedOn = models.DateTimeField
    lastEditedOn = models.DateTimeField

class Score(models.Model):
    jobID = models.OneToOneField(Job, on_delete=models.CASCADE, primary_key=True)
    attractiveness = models.PositiveIntegerField
    importance = models.PositiveIntegerField
    childrenScore = models.PositiveIntegerField
    personnel = ArrayField(models.CharField(max_length=50))
    resources = ArrayField(models.CharField(max_length=50))
    timePeriodBool = models.BooleanField
    timePeriod = models.DurationField
    deadlineBool = models.BooleanField
    deadline = models.DateTimeField
    total = models.PositiveIntegerField

class Dependency(models.Model):
    parent = models.UUIDField
    child = models.UUIDField


