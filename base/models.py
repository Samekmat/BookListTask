from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=120)
    publish_date = models.CharField(max_length=30)
    ISBN = models.CharField(max_length=200)
    num_of_pages = models.IntegerField(null=True)
    cover_link = models.URLField(default='', blank=True)
    publish_lang = models.CharField(max_length=100)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title
