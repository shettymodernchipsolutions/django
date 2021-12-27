from django.shortcuts import render
from movie.models import MovieTable
from movie.forms import MovieTableForm


# Create your views here.


def home_page(request):
    return render(request=request, template_name='movie/homepage.html')


def add_movie(request):
    movie_form = MovieTableForm

    my_dict = {'movie_form': movie_form}
    return render(request=request, template_name='movie/add.html', context=my_dict)]


def movie_list(request):
    movie_data = Moviedetails.objects.all()
    my_dict = {'movie_data': movie_data}
    return render(request=request, template_name='movie/list.html', context=my_dict)