"""
Aplicativo CLI para cálculos em operações de mercado
"""

import click
from em import em
from pt import pt
from cfd import cfd
from mg import mg
from sw import sw
from pm import pm


@click.group()
def op():
    """Calculos para operacoes de trading"""
    pass


op.add_command(em)
op.add_command(pt)
op.add_command(cfd)
op.add_command(mg)
op.add_command(sw)
op.add_command(pm)


if __name__ == "__main__":
    op()
