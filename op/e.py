"""
Calcula uma operação de trading
"""

import click


@click.command()
@click.argument("entrada", type=float)
@click.option("--risco", "-r", type=float)
@click.option("--retorno", "-rr", type=int)
@click.option("--digitos", "-d", type=int, default=0)
@click.option("--tipo", "-t", default="c")
def e(entrada, risco, retorno, digitos, tipo):
    """Calcula operacao de trading"""
    if tipo == "v":
        entrada = -entrada  # somente para operação de venda
    sl = entrada - risco  # stop loss
    targets = []
    for rr in range(retorno):
        targets.append(entrada + risco * (rr + 1))
    i = len(targets)
    for tg in reversed(targets):
        click.echo("%.{0}f %iX".format(digitos) % (abs(tg), i))
        i -= 1
    click.echo("%.{0}f E".format(digitos) % abs(entrada))
    click.echo("%.{0}f SL".format(digitos) % abs(sl))


if __name__ == "__main__":
    e()
