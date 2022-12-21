from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog', include("blog.urls")) # e.g: http://localhost:8000/blog/posts/my-first-post
]