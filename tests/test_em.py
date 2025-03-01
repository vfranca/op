from click.testing import CliRunner
from op.op import op


run = CliRunner()


def test_calcula_expectativa_matematica():
    res = run.invoke(op, ["em", "60", "300", "150"])
    assert res.output == "operacoes 10\nlucro medio 120.00\nlucro total 1200.00\n"


def test_calcula_expectativa_matematica_com_opcao_operacoes():
    res = run.invoke(op, ["em", "--operacoes", "40", "60", "300", "150"])
    assert res.output == "operacoes 40\nlucro medio 120.00\nlucro total 4800.00\n"
