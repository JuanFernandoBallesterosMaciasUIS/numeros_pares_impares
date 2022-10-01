# Numeros positivos pares y impares

print("-------------------------------------------")
print("-----------------PAR-IMPAR-----------------")
print("-------------------------------------------")

# input
n = int(input("Digite un número entero positivo: "))

# process
par = 0
impar = 0

while n != 0:
    n1 = n % 2
    if n1 == 0:
        par = par + 1
    else:
        impar = impar + 1
    n = int(input("Digite otro número entero positivo: "))
else:
    print("Cantidad de números pares:",par)
    print("Cantidad de números impares:",impar)