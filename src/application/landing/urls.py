from django.urls import path

from application.landing.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(),name="index"),
]
