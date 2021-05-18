from django.db import models


# Create your models here.
class book(models.Model):
    book_name = models.CharField(max_length=250)
    book_img = models.ImageField(upload_to='picture')
    book_price = models.TextField()


def __str__(self):
    return self.name
