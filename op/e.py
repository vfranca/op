"""
Calcula uma operação de trading
"""

import click


@click.command()
@click.argument("entrada", type=float, envvar="E")
@click.option(
    "--risco", "-r", type=float, envvar="R", help="Risco da operacao em pontos"
)
@click.option(
    "--retorno",
    "-rr",
    type=int,
    default=2,
    envvar="RR",
    help="Risco/retorno da operacao",
)
@click.option(
    "--digitos",
    "-d",
    type=int,
    default=0,
    envvar="DIGITOS",
    help="Digitos depois do separador decimal",
)
@click.option(
    "--compra", "-c", "tipo", flag_value="c", default=True, help="Operacao de compra"
)
@click.option("--venda", "-v", "tipo", flag_value="v", help="Operacao de venda")
@click.option(
    "--target", "-tg", type=float, envvar="TG", default=0, help="Alvo da operação"
)
def e(entrada, risco, retorno, digitos, tipo, target):
    """Calcula operacao de trading"""
    if tipo == "v":
        entrada = -entrada  # somente para operação de venda
    if target:
        target_pontos = abs(target - entrada)
        click.echo("%.{0}f/%.{0}f target".format(digitos) % (target, target_pontos))
    sl = entrada - risco  # stop loss
    targets = []
    for rr in range(retorno):
        targets.append(entrada + risco * (rr + 1))
    i = len(targets)
    for _tg in reversed(targets):
        click.echo("%.{0}f %iX".format(digitos) % (abs(_tg), i))
        i -= 1
    click.echo("%.{0}f E".format(digitos) % abs(entrada))
    click.echo("%.{0}f SL".format(digitos) % abs(sl))


if __name__ == "__main__":
    e()
