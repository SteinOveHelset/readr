from django.db import models

from author.models import Author


class Book(models.Model):
    WANTED = 'wanted'
    WAITING = 'waiting'
    READING = 'reading'
    READ = 'read'

    STATUS_CHOICES = (
        (WANTED, 'Wanted'),
        (WAITING, 'Waiting'),
        (READING, 'Reading'),
        (READ, 'Read')
    )

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=WAITING)

    class Meta:
        ordering = ('title',)