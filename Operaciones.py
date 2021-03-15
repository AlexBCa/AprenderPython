class Operaciones:


    def suma(self, num1, num2):
        try:
            suma = num1 + num2
            return suma

        except TypeError:
            print("Error: Tipo de dato no válido")
            return None

    def resta(self, num1, num2):

        try:
            resta = num1 - num2
            return resta

        except TypeError:
            print("Error: Tipo de dato no válido")
            return None
        except ZeroDivisionError:
            print("Error: No es posible dividir entre cero")
            return None

    def producto(self, num1, num2):
        try:
            producto = num1 * num2
            return producto

        except TypeError:
            print("Error: Tipo de dato no válido")
            return None
