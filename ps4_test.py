from ps4 import convertir_fecha

def test_imprimir_caracteres_impares():
    assert convertir_fecha("06/08/05") == "06 de Agosto de 2005"
    assert convertir_fecha("15/03/95") == "15 de Marzo de 1995"
    assert convertir_fecha("23/11/22") == "23 de Noviembre de 2022"
    assert convertir_fecha("01/09/20") == "01 de Septiembre de 2020"
    assert convertir_fecha("30/04/18") == "30 de Abril de 2018"
    assert convertir_fecha("32/01/20") == "Fecha inválida"
    assert convertir_fecha("15/13/20") == "Fecha inválida"
    assert convertir_fecha("15-03-20") == "Formato de fecha inválido"
    assert convertir_fecha("1a/0b/20") == "Formato de fecha inválido"
    assert convertir_fecha("30/09/23") == "30 de Septiembre de 2023"
    assert convertir_fecha("") == "Formato de fecha inválido"
    assert convertir_fecha("1/1/20") == "Formato de fecha inválido"
    assert convertir_fecha("01/01/2020") == "Formato de fecha inválido"