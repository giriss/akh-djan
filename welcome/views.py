# Create your views here.
from django.http import HttpResponse


def index(request):
    name = "Akhilesh"
    return HttpResponse("Welcome "+name)