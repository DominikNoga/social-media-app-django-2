from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.name


class Enemy(models.Model):
    name = models.CharField(max_length=40, null=True)
    strength = models.IntegerField(null=True)

    def __str__(self):
        return self.name
