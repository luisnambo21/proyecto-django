from django.shortcuts import render
from .models import Cursos
from .forms import ComentarioFormulario
from .models import ComentarioForm
from .forms import ComentarioFormCurso
from .models import ComentarioCurso
from django.shortcuts import get_object_or_404
import datetime
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages

# Create your views here.
def cursos(request):
    cursos=Cursos.objects.all()
    return render(request,"cursos/pagina.html",{'cursos':cursos})

def formulario(request):
    return render(request,"cursos/formulario.html")

def formularioCurso(request):
    return render(request,"cursos/formularioCurso.html")

def registrar(request):
    if request.method == 'POST':
        form = ComentarioFormulario(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
                form.save() #inserta
                comentarios=ComentarioForm.objects.all()
                return render(request,"cursos/ConsultaFormulario.html",
                    {'comentarios':comentarios})    
    form = ComentarioFormulario()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'cursos/formulario.html',{'form': form}) 

def registrarCurso(request):
    if request.method == 'POST':
        form = ComentarioFormCurso(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            comentarios=ComentarioCurso.objects.all()
            return render(request,"cursos/consultasCurso.html",
                {'comentarios':comentarios})
    form = ComentarioFormCurso()
    return render(request,'cursos/formularioCurso.html',{'form': form}) 

def consultarComentarioForm(request):
    comentarios=ComentarioForm.objects.all()
    #all recupera todos los objetos del modelo (registros de la tabla
    #comentariosContacto)
    return render(request,"cursos/ConsultaFormulario.html",{'comentarios':comentarios})
    #Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de comentarios recuparados.


def consultarComentarioCurso(request):
    comentarios=ComentarioCurso.objects.all()
    #all recupera todos los objetos del modelo (registros de la tabla
    #comentariosContacto)
    return render(request,"cursos/ConsultasCurso.html",{'comentarios':comentarios})
  

def eliminarComentarioForm(request, id,
        confirmacion='cursos/confirmarEliminacion.html'):
        comentario = get_object_or_404(ComentarioForm, id=id)
        if request.method=='POST':
            comentario.delete()
            comentarios=ComentarioForm.objects.all()
            return render(request,"cursos/ConsultaFormulario.html",
                {'comentarios':comentarios})

        return render(request, confirmacion, {'object':comentario})

def eliminarCurso(request, id,
        confirmacion='cursos/eliminarCurso.html'):
        comentario = get_object_or_404(ComentarioCurso, id=id)
        if request.method=='POST':
            comentario.delete()
            comentarios=ComentarioCurso.objects.all()
            return render(request,"cursos/ConsultasCurso.html",
                {'comentarios':comentarios})
        return render(request, confirmacion, {'object':comentario})

def consultarComentario(request, id):
        comentario=ComentarioForm.objects.get(id=id)
        return render(request,"cursos/EditarFormulario.html",
                {'comentario':comentario})

def consultarComentarioIndividual(request, id):
        comentario=ComentarioCurso.objects.get(id=id)
        return render(request,"cursos/editarCurso.html",
                {'comentario':comentario})

def editarComentarioContacto(request, id):
        comentario = get_object_or_404(ComentarioForm, id=id)
        form = ComentarioFormulario(request.POST, instance=comentario)

        if form.is_valid():
                form.save() 
                comentarios=ComentarioForm.objects.all()
                return render(request,"cursos/ConsultaFormulario.html",
                        {'comentarios':comentarios})

        return render(request,"cursos/EditarFormulario.html",
                {'comentario':comentario})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo,
            archivo=archivo)
            insert.save()
            return render(request,"cursos/archivos.html")
        else:
                messages.error(request, "Error al procesar el formulario")
    else:
        return render(request,"cursos/archivos.html",{'archivo':Archivos})

def editarComentarioCurso(request, id):
        comentario = get_object_or_404(ComentarioCurso, id=id)
        form = ComentarioFormCurso(request.POST, instance=comentario)

        if form.is_valid():
            form.save() #si el registro ya existe, se modifica.
            comentarios=ComentarioCurso.objects.all()
            return render(request,"cursos/consultasCurso.html",
                    {'comentarios':comentarios})

        return render(request,"cursos/editarCurso.html",
                {'comentario':comentario})

