import openai
from django.apps import AppConfig

from server.settings import embed_model


class ApiConfig(AppConfig):
    """
    AppConfig for the 'api' app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

    def ready(self):
        import api.signals
