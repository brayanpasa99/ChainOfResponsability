from Procesador import Procesador


class Teclado(Procesador):
    """
    Handle request, otherwise forward it to the successor.
    """

    def manejaProcesos(self, nombrePeticion):
        if nombrePeticion == "Escribir":
            print "El teclado puede escribir en pantalla"
            print "Atendiendo la solicitud"
            print "El caracter se ha escrito en pantalla"

        elif self._siguiente is not None:
            self._siguiente.manejaProcesos(nombrePeticion)
        else:
            print "NO"
