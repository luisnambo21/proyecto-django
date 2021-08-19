from django.contrib import admin
from .models import Cursos
from .models import Comentario
from .models import ComentarioForm
from .models import ComentarioCurso


# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields= ('created' , 'updated')
    list_display = ('materiaMayus','horas','aprobado','turno','inicio','fin','created')
    search_fields = ('materia','horas','aprobado','turno','inicio','fin')
    date_hierarchy = 'created'
    list_filter = ('materia','turno')
    list_per_page=2
    ordering=('materia',)
    list_editable=('turno',)
    list_display_links =('horas',)

    fieldsets = (
        (None, {
            'fields' : ('materia',)
        }),
        ('Opciones avanzadas', {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields' : ('horas', 'aprobado', 'turno', 'inicio', 'fin', 'imagen')
        })
    )

    def materiaMayus(self, obj):
        return obj.materia.upper()

    materiaMayus.short_description='MAT'

    
        
    def get_readonly_fields(self, request, obj=None):
#si el usuario pertenece al grupo de permisos "Usuario"
        if request.user.groups.filter(name="Usuarios").exists():
#Bloquea los campos
            return ('aprobado','inicio', 'fin')
#Cualquier otro usuario que no pertenece al grupo "Usuario"
        else:
#Bloquea los campos
            return ('created', 'updated')

admin.site.register(Cursos, AdministrarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(Comentario, AdministrarComentarios)

class AdministrarComentariosCurso(admin.ModelAdmin):
    list_display = ('id', 'matricula')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
admin.site.register(ComentarioCurso, AdministrarComentariosCurso)

class AdministrarComentarioForm(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(ComentarioForm, AdministrarComentarioForm)
