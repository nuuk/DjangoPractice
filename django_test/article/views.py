from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    name = "Mitch"
    html = "<html><body>Hi %s, this seems to have worked!</body></html>" % name
    return HttpResponse(html)