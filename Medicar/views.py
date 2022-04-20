from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from Medicar.models import Medico, Agenda, Consulta
from .serializers import MedicoSerializer, AgendaSerializer, ConsultaSerializer
from rest_framework import permissions
import datetime

from .filters import MedicoFilter, AgendaFilter

class MedicoViewSet(ReadOnlyModelViewSet):
        """
        list: Retorna uma lista com todos o médicos cadastrados.
        read: Necessário informar o id do médico como parâmetro na url, e retorna as informações detalhadas do médico
        """

        queryset = Medico.objects.all()
        serializer_class = MedicoSerializer
        filter_class = MedicoFilter
        filterset_fields = ['nome', 'crm']
        

class AgendaViewSet(ReadOnlyModelViewSet):
        """
        list: Retorna uma lista com todas as agendas disponíveis.
        read: Necessário informar o id da agenda como parâmetro na url, e retorna as informações detalhadas da agenda
        """
        queryset = Agenda.objects.all()
        serializer_class = AgendaSerializer
        filter_class = AgendaFilter
        filterset_fields = ['medico']

        def get_queryset(self):
                data_atual = datetime.date.today()
                return Agenda.objects.all().filter(dia__gte=data_atual)

        
class ConsultaViewSet(ModelViewSet):
        """
        list: Retorna uma lista com todas as consultas marcadas para o paciente. Não exibe consultas passadas.
        read: Necessário informar o id da consulta como parâmetro na url e retorna as informações da consulta.
        create: Cria uma nova consulta para o paciente. Retorna a consulta marcada.
        update: Atualiza uma consulta já marcada para paciente. Necessário informar o id da consulta como parâmetro na url. Retorna a consulta atualizada
        partial_update: Atualiza uma consulta já marcada para paciente. Necessário informar o id da consulta como parâmetro na url. Retorna a consulta atualizada.
        delete: Deleta uma consulta para paciente. Necessário informar o id da consulta como parâmetro na url. Retorna a lista de consultas marcadas para o paciente.
        """
        serializer_class = ConsultaSerializer
        permission_classes = [permissions.IsAuthenticated]

        def get_queryset(self):
                paciente = self.request.user
                data_atual = datetime.date.today()
                queryset = Consulta.objects.all().filter(paciente=paciente, dia__gt=data_atual, esta_disponivel = True)

                return queryset
