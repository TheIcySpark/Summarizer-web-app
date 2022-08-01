from django.db import models


class Topic(models.Model):
    topic = models.CharField(max_length=200)


class SearchQuery(models.Model):
    author = models.CharField(max_length=65)
    title = models.CharField(max_length=200)
    topics = models.ManyToManyField(Topic)
    pages = models.IntegerField()


