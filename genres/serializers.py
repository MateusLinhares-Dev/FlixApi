#Serializer dos genêros
from rest_framework import serializers
from genres.models import Genre

#traz alguma heranças prontas para o serializador, modo serializador
class  GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'