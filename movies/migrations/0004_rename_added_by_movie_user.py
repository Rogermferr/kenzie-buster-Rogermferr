# Generated by Django 4.2.2 on 2023-06-15 20:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0003_rename_user_movie_added_by"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movie",
            old_name="added_by",
            new_name="user",
        ),
    ]
