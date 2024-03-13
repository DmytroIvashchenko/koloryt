from django.urls import path

from collect import views

app_name = 'main'

urlpatterns = [
    path('', views.collect, name='collect'),
]
