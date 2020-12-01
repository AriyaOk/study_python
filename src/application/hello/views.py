from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
#from django.contrib.sessions.models import Session

def view_hello_index(request: HttpRequest) -> HttpResponse:

    name = request.session.get("name")
    address = request.session.get("address")
    about = request.session.get("about")

    context = {
        "address_header": address or "XZ",
        "address_value": address or "",
        "name_header": name or "Anon",
        "name_value": name or "",
        "about_header": about or "no information",
        "about_value": about or "",
    }
    response = render(request, "hello/index.html", context=context)
    return response


def view_hello_greet(request: HttpRequest) -> HttpResponse:
    name = request.POST.get("name")
    address = request.POST.get("address")
    about = request.POST.get("about")

    request.session["name"] = name
    request.session["address"] = address
    request.session["about"] = about

    return redirect("/h/")


def view_hello_reset(request: HttpRequest) -> HttpResponse:

    request.session.clear()
    #session_key = request.session.session_key
    #if session_key != None:
    #    session = Session.objects.get(session_key=session_key)
    #    Session.objects.filter(session_key=session).delete()
    return redirect("/h/")
