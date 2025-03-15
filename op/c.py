"""
Calcula uma conta de trading
"""

import click


@click.command()
@click.argument("saldo", type=float)
@click.option(
    "--risco",
    "-r",
    type=float,
    default=1,
    envvar="RISCO",
    help="Risco por operacao, em porcentagem, default 1.",
)
@click.option(
    "--meta",
    "-m",
    type=int,
    default=30,
    envvar="META",
    help="Meta de ganho, em porcentagem, default 30.",
)
@click.option(
    "--drawdown-maximo",
    "-dm",
    type=int,
    default=60,
    envvar="DM",
    help="Rebaixamento maximo do maior saldo, em porcentagem, default 60.",
)
@click.option(
    "--drawdown-diario",
    "-dd",
    type=int,
    default=10,
    envvar="DD",
    help="Rebaixamento máximo no dia, em porcentagem, default 10.",
)
def c(saldo, risco, meta, drawdown_maximo, drawdown_diario):
    """Calcula uma conta de trading."""
    # Drawdown máximo
    dm = saldo * (drawdown_maximo / 100)
    # Drawdown diário
    dd = saldo * (drawdown_diario / 100)
    # Risco por operação
    r = saldo * (risco / 100)
    # Meta de ganho
    m = saldo * (meta / 100)
    click.echo("saldo da conta %.2f" % saldo)
    click.echo("meta %.2f (%i%%)" % (m, meta))
    click.echo("risco por operacao %.2f %.1f%%" % (r, risco))
    click.echo("drawdown maximo %.2f %i%%" % (dm, drawdown_maximo))
    click.echo("drawdown diario %.2f %i%%" % (dd, drawdown_diario))


if __name__ == "__main__":
    c()
