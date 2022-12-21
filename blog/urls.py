from django.urls import path
from . import views


urlspattern = [
    path("/", views.starting_page, name="starting-page"), 
    path("/posts", views.posts, name="posts-page"), 
    path("/posts/<slug:slug>", views.single_post, name="single-post-page") #/posts/my-first-post 
]