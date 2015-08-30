from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Device(models.Model):
    name = models.CharField(max_length=255,default=None)
    type = models.CharField(max_length=255,default="", blank=True)
    user = models.ForeignKey(User)


class Expense(models.Model):
    value = models.DecimalField(max_digits=255,decimal_places=2)
    category = models.CharField(max_length=255,default="")
    country = models.CharField(max_length=255,default="", blank=True)
    city = models.CharField(max_length=255,default="", blank=True)
    date = models.DateField(default=datetime.now, blank=True)
    reimbursed = models.BooleanField(default=False)

    user = models.ForeignKey(User)
    device = models.ForeignKey(Device,default=None)
