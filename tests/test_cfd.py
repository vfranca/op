from click.testing import CliRunner
from op import op

run = CliRunner()


def test_calcula_valor_do_cfd():
    res = run.invoke(op, ["cfd", "1", "0.1", "40"])
    assert res.output == "4.00\n"
