from django.urls import path
from . import views

urlpatterns = [
    path("recommendations",views.recommend_courses, name="recommend_courses"),
    path("upload-certificate",views. upload_certificate, name="upload_certificate"),
]