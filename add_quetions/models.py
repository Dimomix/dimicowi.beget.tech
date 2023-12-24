from django.db import models

class Subjects(models.Model):
    name = models.CharField(max_length = 50)

class Category(models.Model):
    name = models.CharField(max_length = 50)

class Score(models.Model):
    name = models.CharField(max_length = 30)
    score = models.IntegerField()

class Questions(models.Model):
    subject = models.ForeignKey(Subjects, on_delete = models.CASCADE, related_name = 'subject')
    category = models.ForeignKey(Category,on_delete = models.CASCADE, related_name = 'category')
    question = models.JSONField()
    answer = models.CharField(max_length = 50)
    score = models.ForeignKey(Score, on_delete = models.CASCADE, related_name = 'questions_score',null = True)