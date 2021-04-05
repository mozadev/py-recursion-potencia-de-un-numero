# def potencia(n):
#     if n==0:
#         return 1
#     else:
#         return 2*potencia(n-1)
#
# n=int(input("ingrese numero: "))
#
# resultado =potencia(n)
# print(resultado)

class Recursividad:
    def potencia(self, n):
        if n == 0:
            return 1
        else:
            return 2 * self.potencia(n - 1)

recursi= Recursividad()
resultasdo=recursi.potencia(2)
print(resultasdo)

lista=['python','es']
cadena='-'.join(lista)
print(cadena)
print(lista)