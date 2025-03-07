from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipo
from .forms import EquipoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def registro_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después del registro
            messages.success(request, "Registro exitoso. Bienvenido, {}!".format(user.username))
            return redirect("lista_equipos")  # Ahora redirige a la lista de equipos
        else:
            for field in form.errors:
                for error in form.errors[field]:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserCreationForm()
    
    return render(request, "equipos/registro.html", {"form": form})

@login_required(login_url='/login/')  # Redirige al login si el usuario no está autenticado
def index(request):
    return render(request, 'equipos/index.html')


@login_required
def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos/lista_equipos.html', {'equipos': equipos})

@login_required
def agregar_equipo(request):
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Equipo agregado exitosamente.")
            return redirect('lista_equipos')
        else:
            messages.error(request, "Hubo un error al agregar el equipo.")
    else:
        form = EquipoForm()
    return render(request, 'equipos/agregar_equipo.html', {'form': form})

@login_required
def editar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    if request.method == "POST":
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            messages.success(request, "Equipo actualizado correctamente.")
            return redirect('lista_equipos')
        else:
            messages.error(request, "Hubo un error al actualizar el equipo.")
    else:
        form = EquipoForm(instance=equipo)
    return render(request, 'equipos/editar_equipo.html', {'form': form, 'equipo': equipo})

@login_required
def eliminar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    if request.method == "POST":
        equipo.delete()
        messages.success(request, "Equipo eliminado correctamente.")
        return redirect('lista_equipos')
    return render(request, 'equipos/eliminar_equipo.html', {'equipo': equipo})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Inicio de sesión exitoso.")
            return redirect("lista_equipos")  # Redirige a la lista de equipos después de iniciar sesión
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "equipos/login.html")

def logout_view(request):
    logout(request)
    messages.info(request, "Sesión cerrada correctamente.")
    return redirect("login")  # Redirige a la página de inicio de sesión
