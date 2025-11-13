from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username



class Package(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    days = models.IntegerField()

    def __str__(self):
        return self.title
