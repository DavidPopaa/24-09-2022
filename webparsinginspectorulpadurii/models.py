from django.db import models

class MetriCubiModel(models.Model):
    array_de_metri_cubi = models.CharField(max_length=100)
    
    def __str__(self):
        return "array-ul de metri cubi: " + self.array_de_metri_cubi
    
class IstoricMetriCubi(models.Model):
    nr_inmatriculare = models.CharField(max_length=100)
    volum_detectat = models.CharField(max_length=100)
    volum_avizat = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
   
    
    def __str__(self):
        return "volum detectat: " + str(self.volum_detectat) + "volum avizat: "+ str(self.volum_avizat)
    
class NotOkMetriCubi(models.Model):
    nr_inmatriculare = models.CharField(max_length=100)
    volum_detectat = models.CharField(max_length=100)
    volum_avizat = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return "volum detectat: " + str(self.volum_detectat) + "volum avizat: "+ str(self.volum_avizat)