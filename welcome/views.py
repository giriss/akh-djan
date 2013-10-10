# Create your views here.
#from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    name = "Akhilesh"
    return render(request, "welcome/index.html", { 'name' : name })