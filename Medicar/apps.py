from django.apps import AppConfig


class MedicarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Medicar'

    def ready(self):
        from . import signals
