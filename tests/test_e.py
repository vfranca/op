from click.testing import CliRunner
from op.op import op

run = CliRunner()


def test_calcula_uma_compra():
    res = run.invoke(op, ["e", "130200", "-r", "100", "-rr", "2"])
    assert res.output == "130400 2X\n130300 1X\n130200 E\n130100 SL\n"


def test_calcula_uma_venda():
    res = run.invoke(op, ["e", "130200", "-r", "100", "-rr", "2", "--venda"])
    assert res.output == "130000 2X\n130100 1X\n130200 E\n130300 SL\n"
