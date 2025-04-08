from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index-blog"),
    path("posts", views.posts, name="posts-blog"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-blog"),
]
