from django.urls import path
from movies.views import MovieView, MovieByIdView

urlpatterns = [path("movies/", MovieView.as_view()), path("movies/<int:movie_id>/", MovieByIdView.as_view())]