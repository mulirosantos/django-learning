from django.db import models

# Create your models here.

#Creating a Questions model:

class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

#Creating a Choice model:

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)