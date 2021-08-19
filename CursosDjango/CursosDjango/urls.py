"""CursosDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contenido import views
from cursos import views as views_cursos
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_cursos.cursos, name="Pagina"),
    path('formulario/',views_cursos.formulario, name="Formulario"),
    path('cursos/',views.cursos, name="Cursos"),
    path('formulario/',views.formulario, name="Formulario"),
    path('registrar/',views_cursos.registrar, name="Registrar"),
    path('formularioCurso/',views_cursos.formularioCurso, name="Cursos"),
    path('registrarCurso/',views_cursos.registrarCurso, name="RegistrarCurso"),
    path('consultarComentarioCurso/',views_cursos.consultarComentarioCurso, name="Comentarios2"),
    path('consultarComentarioForm/',views_cursos.consultarComentarioForm, name="Comentarios"),
    path('eliminarComentario/<int:id>/',views_cursos.eliminarComentarioForm, name='Eliminar'),
    path('eliminarCurso/<int:id>/',views_cursos.eliminarCurso, name='EliminarCurso'),
    path('EditarFormulario/<int:id>/',views_cursos.consultarComentario, name="Consultar"),
    path('editarComentario/<int:id>/',views_cursos.editarComentarioContacto, name="Editar"),
    path('editarCurso/<int:id>/',views_cursos.consultarComentarioIndividual, name='Curso'),
    path('comentarioCurso/<int:id>/',views_cursos.editarComentarioCurso, name="EditarCurso"),
    path('subir',views_cursos.archivos, name="Subir"),
 
]

if settings.DEBUG: 
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
