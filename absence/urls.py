from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_absence, name='submit_absence'),
]