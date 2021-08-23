from django.db import models


class Task(models.Model):
    title = models.CharField('Title', max_length=32)
    task = models.TextField('Description')

    def __str__(self):
        return self.title
