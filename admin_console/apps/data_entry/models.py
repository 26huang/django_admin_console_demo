from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

NAME_CHOICES = (
    ('', 'Blank'),
    ('A', 'Name A'),
    ('B', 'Name B'),
    ('C', 'Name C'),
)

STATUS_CHOICES = (
    ('A', 'Status A'),
    ('B', 'Status B'),
    ('C', 'Status C'),
)


class Object(models.Model):
    name = models.CharField(max_length=1, default='', choices=NAME_CHOICES)

    def __str__(self):
        return '{0}'.format(self.name)


class Position(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    last_active = models.DateTimeField(auto_now=True)  # last modified
    start_time = models.DateTimeField(auto_now_add=True)  # creation time
    status = models.CharField(max_length=1, default='A', choices=STATUS_CHOICES)

    def __str__(self):
        return '{0} position {1}, {2}'.format(self.object, self.latitude, self.longitude)