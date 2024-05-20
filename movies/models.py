from django.db import models
from genres.models import Genre
from actors.models import Actor

class Movie(models.Model):
    title = models.CharField(max_length=500)
    #cASO DELETE ALGO NO MODELS, DEVE SER ALTERADO TAMBÉM NA TABELA MOVIE
    #O related_name, é somente um apelido, onde você pode também chamar ex: Genre.object.all().movies e usar para avaliar todos os filmes relacionado a esse genero
    genre = models.ForeignKey(
                              Genre, 
                              on_delete=models.PROTECT,
                              related_name='movies'
                              )
    release_date = models.DateField(null=True, blank=True)
    # N PARA N sendo que um ator pode atuar em vários filmes, e vários filmes conter esse ator --> ManyToManyField
    actors = models.ManyToManyField(Actor, related_name='movies')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title