from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from movies.models import Movie
from  movies.serializers import MovieSerializer, MovieDetailSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermissionClass
from reviews.models import Review

class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieDetailSerializer
        return MovieSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = Movie.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieDetailSerializer
        return MovieSerializer

class MovieStatisView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
    queryset = Movie.objects.all()

    # somente com a function get, já se baseia que é um method get na request, assim executando a lógica
    def get(self, request):
        total_movies = self.queryset.count()

        #annotate é usado para fazer uma anotação de cada objeto e anexando o resultado ao objeto. aqui por exemplo iremos fazer para cada genero separando por id, estilo JOIN
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        #values em uma queryset, serve para filtrar por coluna

        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg__stars=Avg('stars'))['avg__stars']

        return response.Response(data={
            'total_movies':total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'media_stars': round(average_stars, 1) if average_stars else 0,
        }, status=status.HTTP_200_OK)
    