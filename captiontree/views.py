from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def about(request):
    return HttpResponse("about me")
def css_renderer(request, filename):
    return render(request, filename + '.css', {}, content_type="text/css")