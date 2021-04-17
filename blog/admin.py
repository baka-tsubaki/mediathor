from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'categories', 'author', 'created')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('f_name', 'email', 'subject', 'content')

admin.site.register(Categories)
admin.site.register(Author)