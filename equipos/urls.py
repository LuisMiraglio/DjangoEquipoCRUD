from django.urls import path
from .views import login_view, logout_view, index, agregar_equipo, editar_equipo, eliminar_equipo, lista_equipos, registro_view

urlpatterns = [
    path('', lista_equipos, name='lista_equipos'),
    path('agregar/', agregar_equipo, name='agregar_equipo'),
    path('lista/', lista_equipos, name='lista_equipos'),
    path('editar/<int:equipo_id>/', editar_equipo, name='editar_equipo'),
    path('eliminar/<int:equipo_id>/', eliminar_equipo, name='eliminar_equipo'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path("registro/", registro_view, name="registro"),  # Nueva URL para el registro
]
