"""
Calcula valor do contrato por diferença
"""

import click


@click.command()
@click.argument("pontos", type=float, envvar="R")
@click.argument("volume", type=float, envvar="LOT")
@click.option("--tamanho", "-t", type=float, envvar="TAM", default=100000)
def cfd(pontos, volume, tamanho):
    """Calcula o contrato por diferenca"""
    cfd = pontos * volume * tamanho
    click.echo("%.2f" % cfd)


if __name__ == "__main__":
    cfd()
