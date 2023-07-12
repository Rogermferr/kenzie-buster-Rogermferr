from rest_framework import serializers
from .models import RatingOptions, Movie
from users.models import User


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=None)
    rating = serializers.ChoiceField(choices=RatingOptions.choices, default=RatingOptions.G)
    synopsis = serializers.CharField(default=None)
    added_by = serializers.SerializerMethodField()

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)

    def update(self, instance: Movie, validated_data: dict) -> Movie:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    def get_added_by(self, obj: User):
        return obj.user.email
