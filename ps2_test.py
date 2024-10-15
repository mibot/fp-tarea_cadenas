from ps2 import imprimir_digitos_pares

def test_imprimir_caracteres_impares():
    assert imprimir_digitos_pares("a12bc34de5") == "24"
    assert imprimir_digitos_pares("abcdefg") == ""
    assert imprimir_digitos_pares("1234567") == "1357"
    assert imprimir_digitos_pares("") == ""
    assert imprimir_digitos_pares("0a1b2c3d4e") == "01234"
    cadena_larga = "0123456789" * 3
    assert imprimir_digitos_pares(cadena_larga) == "02468" * 3
    assert imprimir_digitos_pares("1 2 3 4 5") == "12345"
