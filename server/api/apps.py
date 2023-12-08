from django.apps import AppConfig
from .utils.load_embedding_model import load_embedding_model
from server.settings import embed_model
import openai
class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        import api.signals
        openai.api_key = "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"
        embed_model = load_embedding_model()