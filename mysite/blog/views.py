from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello!! This is my first Django app!!")