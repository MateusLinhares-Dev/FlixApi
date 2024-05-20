from django.db import models

#Pré definir os dados do campo nacionalidade QUE SERÃO OS CHOICES, PORÉM ELE SERÁ UMA TUPLA PORÉM OS ITENS NÃO PODE SE REPETIR.
#o valor da esquerda que pertence a tupla dentro de tupla, é o valor que irá aparecer no banco de dados e o da direita será mostrado (valor tratado)

NATIONALITY_CHOICES = (
                        ('USA', 'Estados Unidos'),
                       ('BRAZIL', 'Brasil')
                       )

class Actor(models.Model):
    name = models.CharField(max_length=200)
    #caso não seja declarado o blank e null, por padrão os campos serão obrigatórios.
    birthday = models.DateField(blank=True, null=True)
    #pre definir o que será colocado nesse campo
    nationality = models.CharField(
        max_length=100, 
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True,
        )

    def __str__(self) -> str:
        return self.name