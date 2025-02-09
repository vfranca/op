"""
Calcula valor de CFD de forex
"""

import click


@click.command()
@click.argument("volume", type=float)
@click.argument("range", type=float)
def fx(volume, range):
    """Calcula o CFD de forex."""
    tamanho = 100000
    cfd = range * volume * tamanho
    click.echo("%.2f" % cfd)


if __name__ == "__main__":
    fx()
