from click.testing import CliRunner
from op.op import op

run = CliRunner()


def test_calcula_uma_compra():
    res = run.invoke(op, ["e", "130200", "-r", "100", "-rr", "2"])
    assert res.output == "130400 2X\n130300 1X\n130200 E\n130100 SL\n"
