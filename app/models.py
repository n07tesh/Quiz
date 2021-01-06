from django.db import models

# Create your models here.
class Quiz(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')
    question = models.CharField(max_length = 200)
    choice_one = models.CharField(max_length= 200)
    choice_two = models.CharField(max_length= 200)
    choice_three = models.CharField(max_length = 200)
    choice_four = models.CharField(max_length=200)
    answer = models.CharField(max_length = 200)