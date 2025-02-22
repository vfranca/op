"""
Calcula uma operação de trading
"""

import click


@click.command()
@click.argument("entrada", type=float)
@click.option("--risco", "-r", type=float)
@click.option("--retorno", "-rr", type=int)
@click.option("--digitos", "-d", type=int, default=0)
def e(entrada, risco, retorno, digitos):
    """Calcula operacao de trading"""
    sl = entrada - risco
    targets = []
    for rr in range(retorno):
        targets.append(entrada + risco * (rr + 1))
    i = len(targets)
    for tg in reversed(targets):
        click.echo("%.{0}f %iX".format(digitos) % (tg, i))
        i -= 1
    click.echo("%.{0}f E".format(digitos) % entrada)
    click.echo("%.{0}f SL".format(digitos) % sl)


if __name__ == "__main__":
    e()
