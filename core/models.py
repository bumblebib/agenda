from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100) #cria campo de char com tamanho maximo de 100 caracteres
    descricao = models.TextField(blank=True, null=True) #cria um campo de texto que pode estar vazio ou nulo
    data_evento = models.DateTimeField(verbose_name='Data do Evento') #cria um campo de data que recebe a data do evento
    data_criacao = models.DateTimeField(auto_now=True) #cria um campo de data, que tem a data de criação do evento
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #importa tabela usuarios do django e informando para excluir todos os eventos caso o usuario seja excluido


    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo #retorna o nome do titulo no banco de dados

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M')