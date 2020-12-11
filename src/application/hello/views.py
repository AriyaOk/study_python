from typing import Dict

from django import forms
from django.views.generic import FormView
from django.views.generic import RedirectView


class HelloForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()
    about = forms.CharField()


class HelloView(FormView):
    template_name = "hello/index.html"
    success_url = "/h/"
    form_class = HelloForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.session.get("name")
        address = self.request.session.get("address")
        about = self.request.session.get("about")
        context.update(
            {
                "name": name or "Anon",
                "address": address or "XZ",
                "about": about or "nosing",
            }
        )

        return context

    def get_initial(self, **kwargs):
        return self.get_extended_context()

    def get_extended_context(self, **kwargs) -> Dict:
        name = self.request.session.get("name")
        address = self.request.session.get("address")
        about = self.request.session.get("about")
        context = {
            "address": address,
            "name": name,
            "about": about,
        }
        return context

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        address = form.cleaned_data["address"]
        about = form.cleaned_data["about"]
        self.request.session["name"] = name
        self.request.session["address"] = address
        self.request.session["about"] = about
        return super().form_valid(form)


class HelloReset(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        self.request.session.clear()
        return "/h/"
