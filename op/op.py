"""
Aplicativo CLI para cálculos em operações de mercado
"""

import click
from op.em import em
from op.pt import pt
from op.cfd import cfd
from op.mg import mg
from op.sw import sw
from op.pm import pm
from op.e import e


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
op.add_command(e)


if __name__ == "__main__":
    op()
