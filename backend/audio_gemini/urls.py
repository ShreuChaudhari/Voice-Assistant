from django.urls import path
from . import views

urlpatterns = [
    path('record/', views.record_audio, name='record_audio'),
    path('process/', views.process_text, name='process_text'),
]