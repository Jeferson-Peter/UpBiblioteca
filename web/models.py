from django.db import models
import datetime
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, unique=True)
    author = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return self.title


class BookLoan(models.Model):
    user = models.CharField(max_length=100,null=True, blank=True, unique=True)
    borrowed = models.DateField(default = datetime.date.today,  null=True, blank=True)
    returned = models.DateField(default = datetime.date.today, null=True, blank=True)
    book_id = models.ForeignKey(Book, on_delete=models.DO_NOTHING)

