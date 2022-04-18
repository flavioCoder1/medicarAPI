import django_filters

from Medicar.models import Medico, Agenda

class MedicoFilter(django_filters.FilterSet):
    nome = django_filters.filters.CharFilter(
        lookup_expr='icontains'
    )
    crm = django_filters.filters.CharFilter(
        lookup_expr='icontains'
    )

    class Meta:
        model = Medico
        fields = (
            'nome', 'crm'
        )

class AgendaFilter(django_filters.FilterSet):
    medico = django_filters.filters.ModelMultipleChoiceFilter(
        queryset=Medico.objects.all()
    )

    medico__crm = django_filters.filters.ModelMultipleChoiceFilter(
        queryset=Medico.crm.objects.all(),
    )

    data_inicio = django_filters.DateFilter(field_name='dia', lookup_expr='gte')
    data_final = django_filters.DateFilter(field_name='dia', lookup_expr='lte')

    class Meta:
        model = Agenda
        fields = (
            'medico', 'medico__crm', 'data_inicio', 'data_final'
        )
