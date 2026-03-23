from django.db import models


class Acessorio(models.Model):
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.descricao