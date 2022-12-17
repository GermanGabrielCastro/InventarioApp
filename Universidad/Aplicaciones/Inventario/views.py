from django.shortcuts import render, redirect
from .models import EquiposComputo
from django.contrib import messages

# Create your views here.


def home(request):
    equipos = EquiposComputo.objects.all()
    messages.success(request, '¡Equipos listados!')
    return render(request, "gestionEquipos.html", {"equipos": equipos})


def registrarEquipo(request):
    codigo_activo_fijo = request.POST['txtCodigo']
    tipo = request.POST['txtTipo']
    marca = request.POST['txtMarca']
    modelo = request.POST['txtModelo']
    color = request.POST['txtColor']

    equipo = EquiposComputo.objects.create(codigo_activo_fijo=codigo_activo_fijo, tipo=tipo, marca=marca, modelo=modelo, color=color)
    messages.success(request, '¡Equipo registrado!')
    return redirect('/')


def edicionEquipo(request, codigo_activo_fijo):
    equipo = EquiposComputo.objects.get(codigo_activo_fijo=codigo_activo_fijo)
    return render(request, "edicionEquipo.html", {"equipo": equipo})


def editarEquipo(request):
    codigo_activo_fijo = request.POST['txtCodigo']
    tipo = request.POST['txtTipo']
    marca = request.POST['txtMarca']
    modelo = request.POST['txtModelo']
    color = request.POST['txtColor']

    equipo = EquiposComputo.objects.get(codigo_activo_fijo=codigo_activo_fijo)
    equipo.tipo = tipo
    equipo.marca = marca
    equipo.modelo = modelo
    equipo.color = color
    equipo.save()

    messages.success(request, '¡Equipo actualizado!')

    return redirect('/')


def eliminacionEquipo(request, codigo_activo_fijo):
    equipo = EquiposComputo.objects.get(codigo_activo_fijo=codigo_activo_fijo)
    equipo.delete()

    messages.success(request, '¡Equipo eliminado!')

    return redirect('/')
