from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from ReMarket.session_utils import contar_visita
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

# Vista para registrar nuevos usuarios.
def registro(request):

    # Incrementamos el contador de visitas.
    visitas = contar_visita(request)

    # Creamos el formulario de registro.
    form = UserCreationForm(
        request.POST if request.method == "POST" else None
    )

    # Comprobamos si se ha enviado el formulario y es válido.
    if request.method == "POST" and form.is_valid():

        # Guardamos el nuevo usuario en la base de datos.
        form.save()

        # Redirigimos al usuario al inicio de sesión.
        return redirect("iniciar_sesion")

    # Enviamos el formulario y las visitas al HTML.
    contexto = {
        'form': form,
        'visitas': visitas,
    }

    # Mostramos la página de registro.
    return render(request, "usuarios/registro.html", contexto)


# Vista para iniciar sesión.
def iniciar_sesion(request):

    # Incrementamos el contador de visitas.
    visitas = contar_visita(request)

    # Creamos el formulario de inicio de sesión.
    form = AuthenticationForm(
        request,
        data=request.POST if request.method == "POST" else None
    )

    # Comprobamos si las credenciales son correctas.
    if request.method == "POST" and form.is_valid():

        # Iniciamos la sesión del usuario autenticado.
        login(request, form.get_user())

        # Redirigimos a la página principal.
        return redirect("index")

    # Enviamos el formulario y las visitas al HTML.
    contexto = {
        'form': form,
        'visitas': visitas,
    }

    # Mostramos la página de inicio de sesión.
    return render(request, "usuarios/iniciar_sesion.html", contexto)

@login_required
@permission_required("auth.delete_user", raise_exception=True)
def gestionar_usuarios(request):

    visitas = contar_visita(request)

    # Eliminar usuario si se recibe una petición POST.
    if request.method == "POST":
        usuario_id = request.POST.get("usuario_id", "")

        if usuario_id.isdecimal():
            User.objects.filter(id=usuario_id).exclude(
                id=request.user.id
            ).exclude(is_superuser=True).delete()

        return redirect("gestionar_usuarios")

    # Obtener todos los usuarios.
    lista_usuarios = User.objects.all()

    contexto = {
        'lista_usuarios': lista_usuarios,
        'visitas': visitas,
    }

    return render(request, "usuarios/gestionar.html", contexto)