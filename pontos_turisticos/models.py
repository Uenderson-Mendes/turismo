from django.db import models


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    imagem = models.ImageField(upload_to='pontos/', blank=True, null=True)

    def __str__(self):
        return self.nome
