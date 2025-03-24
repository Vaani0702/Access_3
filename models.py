from django.db import models

class User(models.Model):
    wallet_address = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
