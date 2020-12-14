from django.contrib.auth.views import LoginView
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.utils.http import url_has_allowed_host_and_scheme

from project import settings


class SignInView(LoginView):
    template_name = "onboarding/sign-in.html"
