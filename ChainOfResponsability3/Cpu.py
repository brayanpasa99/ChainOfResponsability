from Procesador import Procesador


class Cpu(Procesador):
    """
    Handle request, otherwise forward it to the successor.
    """

    def manejaProcesos(self, nombrePeticion):
        if nombrePeticion == "Encender":
            print "La CPU puede prender el PC"
            print "Atendiendo la solicitud"
            print "PC encendido, bienvenido"

        elif self._siguiente is not None:
            self._siguiente.manejaProcesos(nombrePeticion)
        else:
            print "Su solicitud no ha podido ser procesada"
