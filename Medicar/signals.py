from django.db.models import signals
from django.dispatch import receiver
from Medicar import models

@receiver(signals.post_save, sender=models.Consulta)
def update_agenda_when_save_consulta(sender, instance, **kwargs):
    consulta = instance
    consulta.esta_disponivel = False
    consulta.save()

@receiver(signals.post_delete, sender=models.Consulta)
def update_agenda_when_delete_consulta(sender, instance, **kwargs):
    consulta = instance
    consulta.esta_disponivel = True
    consulta.save()
