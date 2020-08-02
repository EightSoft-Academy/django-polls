import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # related_name
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


'''References:
1. About q.choice_set.all(): https://docs.djangoproject.com/en/3.0/ref/models/relations/
2. About __startswith, __endswith ... https://docs.djangoproject.com/en/3.0/topics/db/queries/#field-lookups-intro
3. Database API https://docs.djangoproject.com/en/3.0/topics/db/queries/'''
