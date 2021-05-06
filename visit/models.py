from django.db import models

class Visit(models.Model):

    user = models.CharField(max_length=125)
    email = models.CharField(max_length=100)

