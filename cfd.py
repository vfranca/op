"""
Aplicativo CLI para calcular valor do contrato por diferença
"""

import click


@click.command()
@click.argument("tamanho-contrato", type=float)
@click.argument("volume_minimo", type=float)
@click.argument("range", type=float)
def cfd(tamanho_contrato, volume_minimo, range):
    """Calcula o contrato por diferenca"""
    cfd = range * volume_minimo * tamanho_contrato
    click.echo("%.2f" % cfd)


if __name__ == "__main__":
    cfd()
