from django.urls import path
from . import views

app_name='awardapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('calender', views.calender, name='calender'),
    path('contact', views.contact, name='contact'),



]