from rest_framework import generics
from actors.models import Actor
from actors.serializers import SerializerActorModel
#Lista e criar
class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = SerializerActorModel
    
# detail, delete and put
class ActorUpdateRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = SerializerActorModel