num1 = int(input("digite uma nota:"))
num2 = int(input("digite uma nota:"))
num3 = int(input("digite uma nota:"))
num4 = int(input("digite uma nota:"))
soma = num1 + num2 + num3 + num4
media = soma/4
if media < 7:
    print("você está reprovado")
else:
    print("você está aprovado")