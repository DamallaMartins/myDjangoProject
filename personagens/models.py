from django.db import models

# Create your models here.

class Personagem(models.Model):
    nome = models.CharField(max_length=50)
    classe = models.CharField(
        max_length=10,
        choices=[
            ('Guerreiro', 'Guerreiro'),
            ('Mago', 'Mago'),
            ('Arqueiro', 'Arqueiro'),
        ],
    )
    data_de_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} ({self.classe})'
