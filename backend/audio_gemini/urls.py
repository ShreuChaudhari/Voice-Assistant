from django.urls import path
from . import views

urlpatterns = [
    path("process_text/", process_text),
    path("record_audio/", record_audio),
]
