from click.testing import CliRunner
from op import op


run = CliRunner()


def test_calcula_expectativa_matematica():
    res = run.invoke(op, ["em", "60", "300", "150"])
    assert res.output == "operacoes 10\nlucro medio 120.00\nlucro total 1200.00\n"
