
def contar_visita(request):
    # Recuperamos el contador de la sesión.
    # Si todavía no existe, empezamos desde cero.
    visitas = request.session.get('paginas_visitadas', 0)

    # Sumamos una visita cada vez que se ejecuta la función.
    visitas += 1

    # Guardamos el nuevo contador en la sesión.
    request.session['paginas_visitadas'] = visitas

    # Devolvemos el total actualizado.
    return visitas
