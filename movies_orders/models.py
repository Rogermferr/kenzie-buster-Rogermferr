from django.db import models


class MovieOrder(models.Model):
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE, related_name="movies_orders")

    movie_order = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_movies_orders")

    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
