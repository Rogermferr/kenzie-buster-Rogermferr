from django.shortcuts import get_object_or_404
from rest_framework.views import Request, Response, status, APIView
from movies.models import Movie
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import MovieOrderSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request: Request, movie_id: int) -> Response:
        movie_obj = get_object_or_404(Movie, id=movie_id)

        serializer = MovieOrderSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(movie=movie_obj, movie_order=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)
