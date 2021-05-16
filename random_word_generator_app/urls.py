from django.urls import path     
from . import views
urlpatterns = [
    path('', views.random),
    path('random_word', views.random),
    path('random_word/reset_counter', views.reset),
    path('random_word_redirect', views.random_word)
]
