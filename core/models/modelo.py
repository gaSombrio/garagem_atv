from django.db import models


class Modelo(models.Model):
    nome = models.CharField(max_length=80, blank=True, null=True)
    marca = models.CharField(max_length=80, blank=True, null=False)
    categoria = models.CharField(max_length=80, blank=True, null=False)

    def __str__(self):
        nome = (self.nome or '').upper()
        marca = (self.marca or '').upper()
        return f'{self.id} - {marca} - {nome}'
