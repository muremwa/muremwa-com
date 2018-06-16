from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # muremwa.com
    path('', views.main, name="main"),
    # muremwa.com/blogs
    path('blogs/', include("blog.urls")),
]
