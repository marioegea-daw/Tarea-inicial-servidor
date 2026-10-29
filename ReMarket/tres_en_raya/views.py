from django.shortcuts import render


def tres_en_raya(request):
    if request.method == 'POST':
        tablero = list(request.POST.get('tablero', '---------'))
        turno = request.POST.get('turno', 'X')
        posicion = request.POST.get('posicion')

        # Comprobamos que los datos recibidos sean válidos
        if (
            len(tablero) != 9
            or any(c not in 'XO-' for c in tablero)
            or turno not in ('X', 'O')
        ):
            tablero = list('---------')
            turno = 'X'

        terminado = False
        mensaje = f'Turno de {turno}'

        # Comprobamos que la posición sea válida
        if posicion is not None and posicion.isdigit():
            posicion = int(posicion)

            if (
                0 <= posicion < 9
                and tablero[posicion] == '-'
            ):
                tablero[posicion] = turno

                # Comprobamos si alguien ha ganado
                combinaciones = [
                    (0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6),
                ]

                ganador = None

                for a, b, c in combinaciones:
                    if (
                        tablero[a] == tablero[b] == tablero[c]
                        and tablero[a] in ('X', 'O')
                    ):
                        ganador = tablero[a]
                        break

                if ganador:
                    mensaje = f'¡Ha ganado {ganador}!'
                    terminado = True
                elif '-' not in tablero:
                    mensaje = '¡Empate!'
                    terminado = True
                else:
                    turno = 'O' if turno == 'X' else 'X'
                    mensaje = f'Turno de {turno}'

    else:
        tablero = list('---------')
        turno = 'X'
        mensaje = 'Turno de X'
        terminado = False

    contexto = {
        'tablero': tablero,
        'turno': turno,
        'mensaje': mensaje,
        'terminado': terminado,
    }

    return render(request, 'tres_en_raya.html', contexto)
