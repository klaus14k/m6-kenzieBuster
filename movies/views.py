from rest_framework.views import APIView, Request, Response, status
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.models import Movie
from movies.serializers import MovieSerializer
from movies.permissions import IsAdminOrReadOnly

class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, request, self)
        serializer = MovieSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)
    
    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)
    

class MovieByIdView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request, movie_id: str) -> Response:
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({"message": "Movie not found"}, status.HTTP_404_NOT_FOUND)
            
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def delete(self, request: Request, movie_id: str) -> Response:
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({"message": "Movie not found"}, status.HTTP_404_NOT_FOUND)
        
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)