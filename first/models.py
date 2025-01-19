from django.db import models
from django.contrib.auth.models import User

class Expression(models.Model):
    expression = models.CharField(max_length=200)
    result = models.FloatField()

    def __str__(self):
        return f'{self.expression} = {self.result}'

class StrAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_string = models.TextField()
    word_count = models.IntegerField()
    number_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.input_string[:20]}'
