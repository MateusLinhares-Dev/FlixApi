#generics do DRF
from rest_framework import generics
#Models
from genres.models import Genre
#serializer
from genres.serializers import GenreSerializer

class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    #serializador importado
    serializer_class = GenreSerializer

class GenereRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer