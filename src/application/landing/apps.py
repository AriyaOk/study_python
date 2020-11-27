from django.apps import AppConfig


class LandingConfig(AppConfig):
    # name = 'landing'
    label = "landing"
    name = f"application.{label}"
