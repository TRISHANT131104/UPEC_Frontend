import openai
from django.apps import AppConfig

from server.settings import embed_model

from .utils.load_embedding_model import load_embedding_model


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

    def ready(self):
        import api.signals

        openai.api_key = "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"
        embed_model = load_embedding_model()
