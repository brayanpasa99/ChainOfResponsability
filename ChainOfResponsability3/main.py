from Cpu import Cpu
from Teclado import Teclado
from Mouse import Mouse


def main():
    cpuConcreta = Cpu()
    tecladoConcreto = Teclado(cpuConcreta)
    mouseConcreto = Mouse(tecladoConcreto)


    mouseConcreto.manejaProcesos("Presionar")
    mouseConcreto.manejaProcesos("Hola1")
    mouseConcreto.manejaProcesos("Escribir")
    mouseConcreto.manejaProcesos("Hola2")
    mouseConcreto.manejaProcesos("Encender")
    mouseConcreto.manejaProcesos("Hola3")

if __name__ == "__main__":
    main()
