fw = float(input("Insira o peso total do peixe em quilo: "))

if fw < 50:
	print("Peso máximo de peixes não excedido. Não há multa a pagar.")

elif fw > 50:
	excesso = round((fw - 50), 2)
	multa = round((excesso * 4.00), 2)

	print("Peso máximo excedido em",excesso, "quilos. Multa a ser paga é de",multa,"reais.") 


