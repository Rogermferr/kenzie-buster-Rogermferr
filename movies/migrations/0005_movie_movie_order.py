# Generated by Django 4.2.2 on 2023-06-16 12:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies_orders", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movies", "0004_rename_added_by_movie_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="movie_order",
            field=models.ManyToManyField(
                related_name="movies_orders",
                through="movies_orders.MovieOrder",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
