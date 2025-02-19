"""
Calcula o swap
"""

import click
from os import getenv


swc = getenv("swc")
swv = getenv("swv")


@click.command()
@click.argument("volume", type=float)
@click.option("--compra", "-c", type=float, default=swc)
@click.option("--venda", "-v", type=float, default=swv)
def sw(volume, compra, venda):
    """Calcula o swap"""
    swap_compra = volume * compra
    swap_venda = volume * venda
    click.echo("swap de compra %.2f" % swap_compra)
    click.echo("swap de venda %.2f" % swap_venda)


if __name__ == "__main__":
    sw()
