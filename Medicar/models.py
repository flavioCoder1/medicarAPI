from django.db import models
from django.contrib.postgres.fields import ArrayField
from rest_framework import serializers
import datetime

# Create your models here.

class Medico(models.Model):
    nome = models.CharField('Nome',primary_key=True,max_length=120)
    crm = models.IntegerField('CRM', blank=False,null=False,unique=True) #Não pode ter dois CRM iguais
    email = models.EmailField('E-mail',max_length=100)

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'
        ordering = ['nome', 'crm']

class Agenda(models.Model):
    medico = models.ForeignKey(
        Medico, verbose_name='Médico', 
        related_name='agenda',
        on_delete=models.CASCADE
    )
    dia = models.DateField('Dia', blank=False, null=False)
    horarios = ArrayField(models.TimeField('Horários'))
    
    def clean(self):
        data_atual = datetime.date.today()
        hora_atual = datetime.datetime.now().time()
        
        if self.dia < data_atual:
            raise serializers.DjangoValidationError('Não podemos criar agenda para dia passado!')
        if (self.dia == data_atual) and (self.horario < hora_atual):
            raise serializers.DjangoValidationError('Não podemos criar agenda para horario passado!')

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'
        ordering = ['dia', 'horarios']
        unique_together=['medico', 'dia'] # Não deve ser possível criar mais de uma agenda para um médico em um mesmo dia

class Consulta(models.Model):
    dia = models.DateField()
    horario = models.TimeField()
    data_agendamento = models.DateTimeField('Data de agendamento', auto_now_add=True)
    medico = models.ForeignKey(
        Medico, verbose_name='Médico',
        related_name='consultas',
        on_delete=models.CASCADE)
    
    class Meta:
        verbose_name="Consulta"
        verbose_name_plural="Consultas"
        ordering=['dia', 'horario']
        unique_together=['dia', 'horario']