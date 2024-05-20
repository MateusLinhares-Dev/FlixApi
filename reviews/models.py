from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator

#Ele aplica em qual filme será feita avaliação, ligando via chave estrangeira ao filme, colocando em sua conexão N para 1 
class Review(models.Model):
    movie = models.ForeignKey(Movie, 
                              on_delete=models.PROTECT, 
                              related_name='reviews'
                              )
    #validators usado para validar o minimo e máximo a ser inserido
    stars = models.IntegerField(
        validators=[
                    MinValueValidator(0,'Avaliação incorreta - tente entre 0 a 5'), 
                    MaxValueValidator(5, 'Avaliação incorreta - tente entre 0 a 5'),
                    ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.comment