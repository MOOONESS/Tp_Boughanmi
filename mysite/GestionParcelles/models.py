from django.contrib.gis.db import models

class Parcelles(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    # Returns the string representation of the model.
    def __str__(self):
        return self.name