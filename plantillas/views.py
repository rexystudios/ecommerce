from django.shortcuts import render

# Create your views here.
def tienda(request):
    return render(request, "frontEnd/base.html")

def administrador(request):
    return render(request, "backEnd/base.html")