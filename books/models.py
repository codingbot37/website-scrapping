from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    pages = models.CharField(max_length=100)
    author =models.CharField(max_length=200)
    link = models.URLField(max_length=2000, blank=True, null=True, unique=True)

    def __str__(self):
        return self.title


class Price(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=2000, blank=True, null=True, unique=True)

    def __str__(self):
        return self.title


class RatingModel(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=2000, blank=True, null=True, unique=True)

    def __str__(self):
        return self.title

      
    




