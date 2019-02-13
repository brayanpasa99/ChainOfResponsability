from Procesador import Procesador


class Mouse(Procesador):
    """
    Handle request, otherwise forward it to the successor.
    """

    def manejaProcesos(self, nombrePeticion):
        if nombrePeticion == "Presionar":
            print "El mouse puede presionar la pantalla"
            print "Atendiendo la solicitud"
            print "Se ha hecho clic a la pantalla"

        elif self._siguiente is not None:
            self._siguiente.manejaProcesos(nombrePeticion)
        else:
            print "NO"
