from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('Blogs/', views.blogView, name='Blogs'),
    path('Blogs_post/<str:pk>/', views.DescView, name='desc'),
    path('contact-us/', views.contact, name='contact'),
    path('About-us/', views.About, name='About'),
    path('Search/', views.Search, name='Search_post'),
    path('delete-comment/<str:pk>/', views.DeleteComment , name='del_cmt'),
   
]