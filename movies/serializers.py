from django.db.models import Avg
from rest_framework import serializers
from genres.serializers import GenreSerializer
from actors.serializers import SerializerActorModel
from movies.models import Movie

#Serve somente para o método POST agora, usando as validações
class MovieSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_relase_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('Error')
        
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Error txt')
        return value


class MovieDetailSerializer(serializers.ModelSerializer):
    actors = SerializerActorModel(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id','title','genre','actors','realease_date','rate','resume']
    
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg'] # esse campo stars__avg é usado para pegar a média que foi calculada e agregada na tabela, por padrão é usado o nome __avg, pré fixo é definido pelo campo que está sendo colocado a média
        
        if rate:
            return rate

        return None


       # reviews = obj.reviews.all() #lte é uma sintaxe que verifica se é menor, aqui no caso menor ou igual a 3

        # if reviews:
        #     sum_reviews = 0

        #     for review in reviews:
        #         sum_reviews += review.stars

        #     reviews_count = reviews.count()
        #     return round(sum_reviews / reviews_count, 1)
        # return None