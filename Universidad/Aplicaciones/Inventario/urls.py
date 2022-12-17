from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarEquipo/', views.registrarEquipo),
    path('edicionEquipo/<codigo_activo_fijo>', views.edicionEquipo),
    path('editarEquipo/', views.editarEquipo),
    path('eliminacionEquipo/<codigo_activo_fijo>', views.eliminacionEquipo)
]
