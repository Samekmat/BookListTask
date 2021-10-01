from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=120)
    publish_date = models.DateField()  # Available formats from default ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']
    ISBN = models.CharField(max_length=13)
    num_of_pages = models.IntegerField()
    cover_link = models.URLField()
    publish_lang = models.CharField(max_length=100)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title
