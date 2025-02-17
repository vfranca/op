"""
Calcula a expectativa matemática
"""

import click


@click.command()
@click.argument("taxa-acerto", type=int)
@click.argument("lucro", type=float)
@click.argument("prejuizo", type=float)
@click.option("--operacoes", "-o", type=int, default=10)
def em(taxa_acerto, lucro, prejuizo, operacoes):
    """Calcula expectativa matematica do trade system"""
    lucro_medio = (taxa_acerto / 100 * lucro) - ((100 - taxa_acerto) / 100 * prejuizo)
    lucro_total = lucro_medio * operacoes
    click.echo("operacoes %i" % operacoes)
    click.echo("lucro medio %.2f" % lucro_medio)
    click.echo("lucro total %.2f" % lucro_total)


if __name__ == "__main__":
    em()
