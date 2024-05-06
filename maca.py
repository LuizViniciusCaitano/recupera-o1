maca = float()
qmaca = int(input("Digite a quantidade de maçãs a serem compradas: \n"))

if qmaca < 12:
    maca = 0.30
else:
    maca = 0.25

print("você vai comprar ", qmaca, "maçãs, e vai pagar R$", qmaca * maca)