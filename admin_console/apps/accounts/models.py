from django.db import models


# Create your models here.
class Gender(models.Model):
    gender = models.CharField(max_length=6)

    def __str__(self):
        return '{}'.format(self.gender)


class Customer(models.Model):
    name = models.CharField(max_length=200, default='')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} {1}'.format(self.name, self.gender)