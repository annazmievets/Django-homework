from django.db import models

class Expression(models.Model):
    expression = models.CharField(max_length=200)
    result = models.FloatField()
