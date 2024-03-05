from app.funcao import ola

def test_funcao_ola_retorna_jornada():
    saida = ola()
    gabarito = "Bom dia!"
    assert saida == gabarito