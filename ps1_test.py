from ps1 import imprimir_caracteres_impares


def test_imprimir_caracteres_impares():
    assert imprimir_caracteres_impares("abcdefg") == "bdf"
    assert imprimir_caracteres_impares("ab") == "b"
    assert imprimir_caracteres_impares("") == ""
    assert imprimir_caracteres_impares("a") == ""
    assert imprimir_caracteres_impares("a b c d") == "   "

