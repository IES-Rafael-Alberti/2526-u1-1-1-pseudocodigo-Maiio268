# 2) La tabla del número X desde el 1 hasta el 10

n = int(input("Introduce un numero: "))

print("| Tabla del", n, "|")

for tabla in range(1,11):
    print(n, "*", tabla, "=", n*tabla)