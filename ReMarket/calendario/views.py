from datetime import datetime
from django.shortcuts import render


def inicio(request):
    return render(request, 'calendario/index.html')


def calendario(request, fecha):
    # Nombres de los meses en español
    meses = {
        1: 'enero',
        2: 'febrero',
        3: 'marzo',
        4: 'abril',
        5: 'mayo',
        6: 'junio',
        7: 'julio',
        8: 'agosto',
        9: 'septiembre',
        10: 'octubre',
        11: 'noviembre',
        12: 'diciembre',
    }

    try:
        # Convertir el texto recibido a una fecha real
        fecha_convertida = datetime.strptime(fecha, '%d-%m-%Y')

        mi_dia = fecha_convertida.day
        mi_mes = meses[fecha_convertida.month]
        mi_ano = fecha_convertida.year

        mensaje = '¡Que tengas un buen día!'

        return render(
            request,
            'calendario/fecha.html',
            {
                'dia': mi_dia,
                'mes': mi_mes,
                'ano': mi_ano,
                'mensaje': mensaje,
            }
        )

    except ValueError:
        # Se ejecuta si el formato es incorrecto
        # o la fecha no existe, por ejemplo 31-02-2026.
        return render(
            request,
            'calendario/error.html',
            {
                'fecha': fecha,
                'mensaje_error': (
                    'La fecha introducida no es válida. '
                    'Utiliza el formato DD-MM-AAAA y comprueba '
                    'que el día y el mes existan.'
                ),
            },
            status=400
        )
