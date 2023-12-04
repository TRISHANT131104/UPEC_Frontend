from django.apps import AppConfig
from .utils.load_embedding_model import load_embedding_model
from server.settings import embed_model
class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        import api.signals
        embed_model = load_embedding_model()