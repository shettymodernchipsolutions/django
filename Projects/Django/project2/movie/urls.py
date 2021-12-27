from django.urls import path
from movie import views

urlpatterns = [
    path('homepage/', views.home_page),
    path('addmovie/', views.add_movie),
    path('movielist/', views.movie_list),
]