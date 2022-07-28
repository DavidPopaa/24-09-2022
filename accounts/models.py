from django.db import models

class Book(models.Model):
    title = models.TextField(max_length=100, blank=False, null=False)
    

