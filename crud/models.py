from django.db import models

class DetailsModel(models.Model):
    id = models.AutoField(primary_key=True)
    dist1 = models.CharField(max_length=100)
    dist2 = models.CharField(max_length=100)
    dist3 = models.CharField(max_length=100)
    dist4 = models.CharField(max_length=100)
    
    def __str__(self):
        return "Dist1:" + self.dist1 + "Dist2:" + self.dist2 + "Dist3:" + self.dist3 + "Dist4:" + self.dist4