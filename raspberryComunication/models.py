from pyexpat import model
from django.db import models

class RaspberryData(models.Model):
    metri_cubi = models.CharField(max_length=100)
    nr_placuta = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)