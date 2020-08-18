from django.db import models

# Create your models here.


class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Books(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


