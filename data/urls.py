from django.urls import path
from .import views
urlpatterns = [
     path('',views.index,name="home"),
     path('create/',views.create,name='create'),
     path('menu/', views.menu, name='menu'),
     path('first/', views.first, name='first'),
     path("edit/<pk>", views.edit,name="edit"),
     path("delete/<pk>", views.delete,name="delete"),
     path("delete/", views.delete, name="delete"),
     path("edit/", views.edit, name="edit"),
     path("base/", views.base, name="base")
]
