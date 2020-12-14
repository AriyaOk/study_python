from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("application.landing.urls")),
    path("h/", include("application.hello.urls")),
    path("b/", include("application.blog.urls")),
    path("o/", include("application.onboarding.urls")),
    path("", include("social_django.urls")),
]
