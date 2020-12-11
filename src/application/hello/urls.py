from django.urls import path

from application.hello import views
from application.hello.views import HelloReset
from application.hello.views import HelloView

urlpatterns = [
    path("", HelloView.as_view()),
    # path("hello/", views.view_hello_greet),
    path("h_del/", HelloReset.as_view()),
]
