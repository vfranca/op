"""
Aplicativo CLI para calcular o preço médio
"""

import click


@click.command()
@click.argument("e1", type=float, envvar="e1")
@click.argument("e2", type=float, envvar="e2", required=False)
@click.argument("e3", type=float, envvar="e3", required=False)
@click.argument("e4", type=float, envvar="e4", required=False)
@click.argument("e5", type=float, envvar="E5", required=False)
@click.option(
    "--digitos",
    "-d",
    type=int,
    default=2,
    envvar="DIGITOS",
    help="Digito da moeda, default 2.",
)
def pm(e1, e2, e3, e4, e5, digitos):
    """Calcula o preco medio"""
    medio = e1
    if e2:
        medio = (e1 + e2) / 2
    if e3:
        medio = (e1 + e2 + e3) / 3
    if e4:
        medio = (e1 + e2 + e3 + e4) / 4
    if e5:
        medio = (e1 + e2 + e3 + e4 + e5) / 5
    click.echo("%.{0}f".format(digitos) % medio)


if __name__ == "__main__":
    pm()
