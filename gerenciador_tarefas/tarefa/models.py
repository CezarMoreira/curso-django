from django.db import models
from django.utils import timezone
# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(_("categoria"), max_length=100)

 
class tarefa(models.model):
    empresa = models.models.CharField(_("empresa"), max_length=250)
    nome_usuario = models.models.CharField(_("nome do usuario"), max_length=250)
    servico = models.models.CharField(_("serviço"), max_length=250)ico = models.models.CharField(_("nome"), max_length=250)
    descricao = models.models.TextField(_("descriçao"), max_length=250)
    data_criacao = models.DataTimeField(default= timezone.now)
    

