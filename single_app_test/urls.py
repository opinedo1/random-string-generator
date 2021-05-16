from django.urls import path
from . import views

urlpatterns = [
        path('', views.index),
        path('new/', views.new),
        path('create/', views.create),
        path('<int:val>',views.show),
        path('<int:number>/edit', views.edit),
        path('<int:number>/delete', views.destroy),
        ]

