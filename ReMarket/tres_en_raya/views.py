
from django.shortcuts import render
from ReMarket.session_utils import contar_visita


def tres_en_raya(request):

    # Contamos la visita del usuario.
    visitas = contar_visita(request)

    # Si el usuario pulsa una casilla (POST)...
    if request.method == 'POST':

        # Recuperamos el tablero guardado en la sesión.
        # Si no existe, creamos uno vacío.
        tablero = request.session.get(
            'tres_en_raya_tablero',
            list('---------')
        )

        # Recuperamos el turno guardado en la sesión.
        turno = request.session.get('tres_en_raya_turno', 'X')

        # Recuperamos si la partida ya ha terminado.
        terminado = request.session.get('tres_en_raya_terminado', False)

        # Comprobamos que los datos recuperados sean válidos.
        if (
            not isinstance(tablero, list)
            or len(tablero) != 9
            or any(c not in 'XO-' for c in tablero)
            or turno not in ('X', 'O')
        ):
            tablero = list('---------')
            turno = 'X'
            terminado = False

        # Preparamos el mensaje inicial.
        mensaje = f'Turno de {turno}'

        # Recuperamos únicamente la posición enviada por el formulario.
        posicion = request.POST.get('posicion')

        # Comprobamos que la posición sea un número.
        if not terminado and posicion is not None and posicion.isdigit():

            posicion = int(posicion)

            # Comprobamos que esté dentro del tablero y que esté vacía.
            if 0 <= posicion < 9 and tablero[posicion] == '-':

                # Colocamos la ficha del jugador actual.
                tablero[posicion] = turno

                # Combinaciones posibles para ganar.
                combinaciones = [
                    (0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6),
                ]

                ganador = None

                # Comprobamos todas las combinaciones.
                for a, b, c in combinaciones:
                    if (
                        tablero[a] == tablero[b] == tablero[c]
                        and tablero[a] in ('X', 'O')
                    ):
                        ganador = tablero[a]
                        break

                # Si hay ganador, terminamos la partida.
                if ganador:
                    mensaje = f'¡Ha ganado {ganador}!'
                    terminado = True

                # Si no quedan casillas vacías, hay empate.
                elif '-' not in tablero:
                    mensaje = '¡Empate!'
                    terminado = True

                # Si nadie ha ganado, cambiamos de jugador.
                else:
                    turno = 'O' if turno == 'X' else 'X'
                    mensaje = f'Turno de {turno}'

        # Guardamos el tablero actualizado en la sesión.
        request.session['tres_en_raya_tablero'] = tablero

        # Guardamos el turno actualizado en la sesión.
        request.session['tres_en_raya_turno'] = turno

        # Guardamos si la partida ha terminado.
        request.session['tres_en_raya_terminado'] = terminado       

        # Guardamos el mensaje actualizado en la sesión.
        request.session['tres_en_raya_mensaje'] = mensaje
    # Si es una petición GET, comenzamos una partida nueva.
    # Comprobamos si ya existe una partida guardada.
    if 'tres_en_raya_tablero' not in request.session:

        # Si no existe, creamos una partida nueva.
        tablero = list('---------')
        turno = 'X'
        mensaje = 'Turno de X'
        terminado = False

        # Guardamos el estado inicial en la sesión.
        request.session['tres_en_raya_tablero'] = tablero
        request.session['tres_en_raya_turno'] = turno
        request.session['tres_en_raya_terminado'] = terminado
        request.session['tres_en_raya_mensaje'] = mensaje

    else:
        # Si ya existe, recuperamos la partida guardada.
        tablero = request.session['tres_en_raya_tablero']
        turno = request.session['tres_en_raya_turno']
        terminado = request.session['tres_en_raya_terminado']
        mensaje = request.session.get(
            'tres_en_raya_mensaje',
            'Turno de X'
        )

    # Enviamos los datos al HTML para mostrar el tablero.
    contexto = {
        'tablero': tablero,
        'turno': turno,
        'mensaje': mensaje,
        'terminado': terminado,
        'visitas': visitas,
    }

    return render(request, 'tres_en_raya.html', contexto)
