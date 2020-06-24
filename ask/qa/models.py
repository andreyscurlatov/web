from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):

  def new(self):
    return self.order_by('-added_at')

  def popular(self):
    return self.order_by('-rating')


class Question(models.Model):

    objects = QuestionManager()
    title = models.CharField(max_length = 255)
    text = models.CharField(max_length = 255)
    added_at = models.DateTimeField(auto_now = True)
    rating = models.IntegerField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes_set')


class Answer(models.Model):

    text = models.CharField(max_length = 255)
    added_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)


