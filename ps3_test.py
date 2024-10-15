from ps3 import completar_cadena


def test_imprimir_caracteres_impares():
    assert completar_cadena("Hola") == "Hola--------------------------"
    assert completar_cadena("Esta es una cadena de 30 chars.") == "Esta es una cadena de 30 chars"
    assert completar_cadena("Esta es una cadena muy larga que debería ser cortada"), "Esta es una cadena muy larga qu"
    assert completar_cadena("") == "------------------------------"
    assert completar_cadena("Hola    Mundo") == "Hola    Mundo-----------------"
    assert completar_cadena("Python", longitud_maxima=10, caracter_relleno='*') == "Python****"
    assert completar_cadena("Corta", longitud_maxima=8) == "Corta---"