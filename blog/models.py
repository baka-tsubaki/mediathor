from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField


class Author(models.Model):
    name = models.CharField(max_length=100)
    prof_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name




class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    author_pic = models.ImageField(null=True, blank=True)
    created = models.DateTimeField()
    image = models.ImageField(null=True, blank=True)
    content = HTMLField()
    
    @property
    def imageUrl(self):
        try:
            url = self.image
        except:
            url = ''
        return url


    def __str__(self):
        return self.title



