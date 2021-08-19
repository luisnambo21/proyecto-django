from django.shortcuts import render, HttpResponse

# Create your views here.
def pagina(request):
    return render(request,"contenido/pagina.html")

def cursos(request):
    return render(request,"contenido/cursos.html")

def formulario(request):
    return render(request,"contenido/formulario.html")