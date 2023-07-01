from django.contrib import admin
from django.urls import path, include
from project.settings import STATIC_ROOT, STATIC_URL
from . import views

# from project.project.settings import STATIC_ROOT, STATIC_URL
app_nmame = "post"
urlpatterns = [
    path("", views.PostList.as_view(), name="post_list"),
    path('<int:pk>/',views.PostDetail.as_view()),]
