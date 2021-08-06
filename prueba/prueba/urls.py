from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registros import views as views_registros
#Importamos la nueva vista de app registros para poder asignar las rutas de acceso a sus vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_registros.registros, name="Principal"),
    #Indicamos que ahora la ruta de principal.html se encuentra en la view de registros
    path('contacto/',views_registros.contacto, name="Contacto"),
    path('formulario/',views.formulario, name="Formulario"),
    path('ejemplo/',views.ejemplo, name="Ejemplo"),
    path('registrar/',views_registros.registrar, name="Registrar"),
    path('consultarComentario/',views_registros.consultarComentarioContacto, name="Comentarios"),
    path('eliminarComentario/<int:id>/',views_registros.eliminarComentarioContacto, name='Eliminar'),
    path('formEditarComentario/<int:id>/',views_registros.consultarComentarioIndividual, name='ConsultaIndividual'),
    path('editarComentario/<int:id>/',views_registros.editarComentarioContacto, name='Editar'),
    path('consultas1',views_registros.consultar1,name="Consulta"),
    path('consultas2',views_registros.consultar2,name="Consulta2"),
    path('consultas3',views_registros.consultar3,name="Consulta3"),
    path('consultas4',views_registros.consultar4,name="Consulta4"),
    path('consultas5',views_registros.consultar5,name="Consulta5"),
    path('consultas6',views_registros.consultar6,name="Consulta6"),
    path('consultas7',views_registros.consultar7,name="Consulta7"),
    path('consultasSQL',views_registros.consultasSQL,name="sql"),
    path('subir',views_registros.archivos,name="Subir"),
    path('seguridad',views_registros.seguridad,name="Seguridad"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
             document_root=settings.MEDIA_ROOT)