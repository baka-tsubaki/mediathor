from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField


class Author(models.Model):
    name = models.CharField(max_length=100)
    prof_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Categories(models.Model):
    ACTUALITE = 'Actualité'
    LITTERATURE = 'Littérature'
    CULTURE = 'Culture'
    EVENEMENT = 'Evènement'
    BESTSELLERS = 'Best Sellers'

    BLOG_CATEGORY_CHOICES = [
        (ACTUALITE, 'Actualité'),
        (LITTERATURE, 'Littérature'),
        (CULTURE, 'Culture'),
        (EVENEMENT, 'Evènement'),
        (BESTSELLERS, 'Best Sellers'),
    ]
    blog_category_choices = models.CharField(
        max_length=20,
        choices=BLOG_CATEGORY_CHOICES,
        default=ACTUALITE,  
    )

    def __str__(self):
        return self.blog_category_choices

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
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


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    content = models.TextField()


class Contact(models.Model):
    f_name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField()
    subject = models.CharField(max_length=350)
    content = models.TextField()

    def __str__(self):
        return self.f_name + ' ' + self.subject
