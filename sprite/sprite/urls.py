from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path('home/', views.home, name = "home"),
    path('about/', views.about, name = "about"),
    path('news/', views.news, name = "news"),
    path('register/', views.register, name = "register"),
    path('base/', views.base, name = "base"),
    path('admin/', admin.site.urls),
]
