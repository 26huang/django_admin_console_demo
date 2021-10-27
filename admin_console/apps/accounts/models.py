from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Gender(models.Model):
    gender = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return '{}'.format(self.gender)


class ZipCode(models.Model):
    zip_code = models.PositiveIntegerField(default=00000, unique=True, validators=[MaxValueValidator(99999), MinValueValidator(00000)])

    def __str__(self):
        return '{}'.format(self.zip_code)


class Customer(models.Model):
    name = models.CharField(max_length=200, default='')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    zip_code = models.ManyToManyField(ZipCode, through='Status')

    def __str__(self):
        return '{0} {1}'.format(self.name, self.gender)

class Status(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    zip_code = models.ForeignKey(ZipCode, on_delete=models.CASCADE)
    active = models.BooleanField()

    def __str__(self):
        return '{0} {1}'.format(self.customer, self.zip_code, self.active)