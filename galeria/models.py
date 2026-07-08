from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Fotografia(models.Model):

    OPCOES_DE_CATEGORIA = [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta")
    ]

    nome = models.CharField(max_length=100,null=False,blank=False)
    legenda = models.CharField(max_length=150,null=False,blank=False)
    categoria = models.CharField(max_length=150,choices=OPCOES_DE_CATEGORIA, default='')
    descricao = models.TextField(null=False,blank=False)
    fotografia = models.ImageField(upload_to='fotos/%Y/%M/%D/',blank=True)
    publicado = models.BooleanField(default=False)
    data_fotografia = models.DateField(default=datetime.now,blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user',
    )

    def __str__(self):
        return self.nome
    