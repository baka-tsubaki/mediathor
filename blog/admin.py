from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Contact)
admin.site.register(Categories)