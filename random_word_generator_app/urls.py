from django.urls import path     
from . import views
urlpatterns = [
    path('', views.random),
    path('random_word', views.random),
    path('random_word/reset_counter', views.reset),
    path('test_redirect', views.random_word)
    # path('submission', views.submission),
    # path('thanks', views.thanks)
    # this is a parameter passed in view.py
    # path('<str:param_name>', views.name)
]
