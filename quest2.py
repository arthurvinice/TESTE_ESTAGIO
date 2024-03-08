# ******* QUESTÃO 2 *******

a = 0
b = 1
c = 1
n = 0
sequence = []
valor = float(input("Digite um numero: "))
valor = int(valor)
print(a)
print(b)
while(n < valor-2):
    c = a + b
    print(c)
    sequence.append(c)
    a = b
    b = c
    n +=1

if valor in sequence:
    print("O número digitado pertence à sequência")
else:
    print("O número digitado não pertence à sequência")
