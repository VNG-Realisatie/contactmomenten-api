from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = "contactmomenten.utils"

    def ready(self):
        from . import checks  # noqa
