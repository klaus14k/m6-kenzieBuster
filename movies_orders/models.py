from django.db import models

class MovieOrder(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    purchased_at = models.DateTimeField(auto_now_add=True)

    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE, related_name="movie_orders")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_movie_orders")