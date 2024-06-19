from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from actors.models import Actor
from actors.serializers import SerializerActorModel
from app.permissions import GlobalDefaultPermissionClass


#Lista e criar

class ActorCreateListView(generics.ListCreateAPIView):
    #lista de classes de permissão, onde vamos passar as classes de permissão que contém as regras das views
    # para tuplas coloque sempre uma virgula, caso não coloque, ele entende que é uma string
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermissionClass,)
    queryset = Actor.objects.all()
    serializer_class = SerializerActorModel
    
# detail, delete and put
class ActorUpdateRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermissionClass,)
    queryset = Actor.objects.all()
    serializer_class = SerializerActorModel