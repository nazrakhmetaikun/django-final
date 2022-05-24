from django.db import models
from django.contrib.auth.models import User

class UserProfil(User):
    pass

class BookJournalBase(models.Model):
    name = models.CharField(max_length=191)
    price = models.FloatField(max_length=200, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract=True

class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=100)

    def __str__ (self):
        return f'{self.id}:{self.name}'
    
class Journal(BookJournalBase):
    TYPES = (
        (1, 'Bullet'),
        (2, 'Food'),
        (3, 'Travel'),
        (4, 'Sport')
    )
    types = models.IntegerField(choices=TYPES)
    publisher=models.CharField(max_length=100)


