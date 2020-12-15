from django.apps import AppConfig


class LandingConfig(AppConfig):
    # name = 'landing'
    label = "telebot"
    name = f"application.{label}"
