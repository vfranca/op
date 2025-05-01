from click.testing import CliRunner
from op.op import op

run = CliRunner()


def test_calcula_horario_da_barra_no_mercado_europeu():
    res = run.invoke(
        op, ["h", "--horario-abertura", "4", "--barra-inicial", "82", "93"]
    )
    assert res.output == "5:00\n"


def test_calcula_horario_da_barra_no_mercado_americano():
    res = run.invoke(
        op, ["h", "--horario-abertura", "10.5", "--barra-inicial", "187", "198"]
    )
    assert res.output == "11:30\n"


def test_calcula_horario_da_barra_no_mercado_brasileiro():
    res = run.invoke(op, ["h", "--horario-abertura", "9", "--barra-inicial", "1", "12"])
    assert res.output == "10:00\n"
