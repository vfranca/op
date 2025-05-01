"""Calcula o horário das barras."""

import click


@click.command()
@click.argument("bar", type=float)
@click.option("--period", "-p", default="m5", help="Período da barra.")
@click.option("--hora-abertura", "-ha", type=float, default=9)
@click.option("--barra-inicial", "-bi", type=int, default=1)
def h(bar, period, hora_abertura, barra_inicial):
    """Calcula o horário de fechamento da barra."""
    minutos_barra = 5
    if period.upper() == "M3":
        minutos_barra = 3
    elif period.upper() == "M10":
        minutos_barra = 10
    elif period.upper() == "M15":
        minutos_barra = 15
    elif period.upper() == "M20":
        minutos_barra = 20
    elif period.upper() == "M30":
        minutos_barra = 30
    elif period.upper() == "H1":
        minutos_barra = 60
    minutos = (bar - (barra_inicial - 1)) * minutos_barra  # minutos da barra
    horas = minutos / 60  # horas da barra
    horario = horas + hora_abertura  # horário da barra
    minuto = abs(int(horario) - horario)  # minuto da barra
    minuto = round(minuto * 60)  # minuto da barra
    hora = int(horario)  # hora da barra
    click.echo("%iH%i" % (hora, minuto))


if __name__ == "__main__":
    h()
