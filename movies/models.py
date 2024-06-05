from django.db import models

class MovieRatings(models.TextChoices):
    GENERAL = "G"
    PG = "PG"
    PG_THIRTEEN = "PG-13"
    RESTRICTED = "R"
    ADULTS_ONLY = "NC-17"

class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, blank=True, default="")
    rating = models.CharField(max_length=20, choices=MovieRatings.choices, default=MovieRatings.GENERAL)
    synopsis = models.TextField(blank=True, default="")

    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, related_name="movies", null=True)
    order = models.ManyToManyField("users.User", through="movies_orders.MovieOrder", related_name="ordered_books")