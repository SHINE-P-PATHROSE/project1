from django.db import models

class movie_list(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.IntegerField()