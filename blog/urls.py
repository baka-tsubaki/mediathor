from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>', views.post, name='post'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)