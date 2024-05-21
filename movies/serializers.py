from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

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