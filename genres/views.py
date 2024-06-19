#generics do DRF
from rest_framework import generics
#Models
from genres.models import Genre
#serializer
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermissionClass

class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,) #CLASSE DE PERMISSÃO
    queryset = Genre.objects.all()
    #serializador importado
    serializer_class = GenreSerializer

class GenereRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass, ) #CLASSE DE PERMISSÃO
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer