# Solicita um número ao usuário
numero = int(input("Digite um número para calcular a tabuada: "))

# Loop para calcular e exibir a tabuada do número
print(f"Tabuada do {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
