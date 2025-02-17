"""
Calcula valor do contrato por diferença
"""

import click


@click.command()
@click.argument("range", type=float, envvar="R")
@click.argument("volume", type=float, envvar="LOT")
@click.option("--tamanho","-t",  type=float, envvar="TAM", default=100000)
def cfd(range, volume, tamanho):
    """Calcula o contrato por diferenca"""
    cfd = range * volume * tamanho
    click.echo("%.2f" % cfd)


if __name__ == "__main__":
    cfd()
