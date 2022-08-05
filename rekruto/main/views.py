from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h4>Hello<h4>")


def get_message(request):
    name = request.GET.get("name", "Tim")
    message = request.GET.get("message", 'check')
    output = f"<h2>Hello {name}! {message}!</h2>"
    return HttpResponse(output)
