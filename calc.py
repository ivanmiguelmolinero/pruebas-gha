def suma(a, b):
    """
    Función a la que se le pasan 2 números (a y b) y te devuelve su suma.
    Args:
        a (int/float): Primer valor a sumar
        b (int/float): Segundo valor a sumar
    return: a+b
    """
    return a + b


def escribir(fpath,    data_in):
    """
    Función que escribe en un archivo
    Args:
        fpath: path absoluto del archivo
        data_in: información a escribir
    """
    with open(fpath, "w") as file_in:
        file_in.write(data_in)


class calculadora:
    """
    Clase calculadora
    """

    def sumar(x, y):
        """
        Función a la que se le pasan 2 números (x e y) y te devuelve su suma.
        Args:
            x (int/float): Primer valor a sumar
            y (int/float): Segundo valor a sumar
        return: x+y
        """
        return suma(x, y)
