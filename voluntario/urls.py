from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # path's correspondientes a las vistas basadas en funciones (voluntarios)
    path('', views.home, name='home'), # mostrare listado de voluntarios
    path('registrar/', views.registrar, name='registrar'),# registrar un voluntario
    path('editar/<int:id>/', views.editar, name='editar'),# edicion de voluntario
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),# eliminar un voluntario
    path('datos/<int:id>/', views.datos, name = 'datos'), # mostrar datos de cada voluntario

    #path's correspondientes a las vistas basadas en clases (evetnos)
    path('eventos/', EventoListView.as_view(), name = 'ver_eventos'), # ver listado de eventos
    path('agregar/', EventoCreateView.as_view(), name='crear_evento'), # crear un nuevo evento
    path('actualizar/<int:pk>/', EventoUpdateView.as_view(), name='actualizar_evento'),# edditar un evento
    path('borrar/<int:pk>/', EventoDeleteView.as_view(), name='borrar_evento'),# borrar un evento
    path('detalle/<int:pk>/', EventoDetailView.as_view(), name='detalle_eventos'), # detalle de cada evento
]
