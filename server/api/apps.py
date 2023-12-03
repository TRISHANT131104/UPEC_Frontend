from django.apps import AppConfig
from .utils import load_embedding_model

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        import api.signals
        load_embedding_model()