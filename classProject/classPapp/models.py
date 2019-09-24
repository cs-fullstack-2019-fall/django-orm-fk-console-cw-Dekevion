from django.db import models
from django.utils import timezone
# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    pub_date = models.DateField(default=timezone.now)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    date_posted = models.ForeignKey(Author, on_delete=models.CASCADE)