pont = []
a = True
e = int(input("Digite a pontuação (de 0 a 5): "))

if (e < 0) | (e > 5):
    print("Número Inválido")
    a = False

while a:
    for i in range(e):
        pont.append("⭐")
        print(pont[i], end="")
    a = False
