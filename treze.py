height = float(input("Escreva sua altura em metros: "))

print("Você é homem ou mulher?")
morf = input("Digite m para homem e f para mulher: ")

if morf in ['m', 'M']:
	print(round(((72.7 * height) - 58), 2))

elif morf in ['f', 'F']:
	print(round(((62.1 * height) - 44.7), 2))

else:
	print("Letra inválida")
