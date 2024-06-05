from django.urls import path
from movies_orders.views import MovieOrderView

urlpatterns = [path("movies/<int:movie_id>/orders/", MovieOrderView.as_view())]