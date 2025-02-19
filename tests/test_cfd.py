from click.testing import CliRunner
from op.op import op

run = CliRunner()


def test_calcula_cfd_comvariaveis_de_ambiente():
    res = run.invoke(op, ["cfd"])
    assert res.output == "4000000.00\n"


def test_calcula_valor_do_cfd_com_opcao_tamanho():
    res = run.invoke(op, ["cfd", "40", "0.1", "--tamanho", "1"])
    assert res.output == "4.00\n"
