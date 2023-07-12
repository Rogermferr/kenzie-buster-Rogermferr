from rest_framework import serializers
from movies_orders.models import MovieOrder
from users.models import User


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(source="movie.title", read_only=True)

    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    buyed_by = serializers.SerializerMethodField()

    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)

    def get_buyed_by(self, obj: User):
        return obj.movie_order.email
