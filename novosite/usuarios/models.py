from django.db import models

# Create your models here.

class Patrimonio(models.Model):

    STATUS = (
        ('Em uso', 'Em uso'),
        ('Manutenção', 'Manutenção'),
        ('Inativo', 'Inativo'),
    )

    numero_tombamento = models.CharField(
        max_length=30,
        unique=True
    )

    nome = models.CharField(
        max_length=100
    )

    categoria = models.CharField(
        max_length=100
    )

    localizacao = models.CharField(
        max_length=100
    )

    responsavel = models.CharField(
        max_length=100
    )

    data_aquisicao = models.DateField()

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS
    )

    def __str__(self):

        return self.nome