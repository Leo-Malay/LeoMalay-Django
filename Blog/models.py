from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False)
    author = models.CharField(max_length=30, blank=False)
    image = models.ImageField(upload_to='media/IMG/')
    content = models.TextField(blank=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
