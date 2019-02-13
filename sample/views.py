from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Apex up working...</h1>")