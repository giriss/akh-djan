# Create your views here.
from django.http import HttpResponse


def lesson1(request, name="Akh"):
    ret = "Is it " + name
    return HttpResponse(ret)
    
def lesson2(request):
    name = request.post['name']
    ret = "! " + name
    return HttpResponse(ret)
