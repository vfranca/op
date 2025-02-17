from click.testing import CliRunner
from op import op

run = CliRunner()


def test_calcula_valor_do_cfd_com_opcao_tamanho():
    res = run.invoke(op, ["cfd", "40", "0.1", "--tamanho", "1"])
    assert res.output == "4.00\n"
