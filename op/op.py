"""Aplicativo CLI para cálculos em operações de mercado."""

import click

from op.c import c
from op.cfd import cfd
from op.e import e
from op.em import em
from op.h import h
from op.mg import mg
from op.pm import pm
from op.sw import sw


@click.group()
def op():
    """Calculos para operacoes de trading"""
    pass


op.add_command(em)
op.add_command(c)
op.add_command(cfd)
op.add_command(mg)
op.add_command(sw)
op.add_command(pm)
op.add_command(e)
op.add_command(h)


if __name__ == "__main__":
    op()
