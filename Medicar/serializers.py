from rest_framework import serializers
from Medicar.models import Medico, Agenda, Consulta
import datetime

class MedicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medico
        fields = ('__all__')

class AgendaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Agenda
        fields = ('__all__')

class ConsultaSerializer(serializers.ModelSerializer):
    paciente = serializers.HiddenField( default=serializers.CurrentUserDefault() )
    medico = MedicoSerializer(read_only=True)
    
    def validate(self, data):
        data_atual = datetime.date.today()
        hora_atual = datetime.datetime.now().time()
        dia = data['dia']
        horario = data['horario']

        consulta_paciente = Consulta.objects.all().filter(paciente=data['paciente'])

        if dia < data_atual:
            raise serializers.DjangoValidationError('Não foi possível marcar consulta: Dia passado!')
        if (dia == data_atual) and (horario < hora_atual):
            raise serializers.DjangoValidationError('Não foi possível marcar consulta: Horário passado!')
        if consulta_paciente.filter(consulta__dia=dia, consulta__horario=horario):
            raise serializers.DjangoValidationError('Não foi possível marcar consulta: Há uma outra consulta marcada para mesmo dia e horário!')
    
        return data

    class Meta:
        model = Consulta
        fields = ('id', 'dia', 'horario', 'data_agendamento', 'medico', 'paciente')
