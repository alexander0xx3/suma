class OperecionesAritemeticas():
    def CalcularSuma(self, sumando1, sumando2):
        return sumando1 + sumando2


    def leerSumandos(self):
        sumando1 = int(input("primer sumando:    "))
        sumando2 = int(input("segundo sumando:    "))
        return sumando1, sumando2


if __name__ == '__main__':
    operacion = OperecionesAritemeticas()
    sumando1, sumando2 = operacion.leerSumandos()
print(f"{sumando1}+{sumando2}={operacion.CalcularSuma(sumando1, sumando2)}")
