altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilogramas: "))

imc = peso / (altura ** 2)
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    classificacao = "Peso normal"
elif 25 <= imc < 30:
    classificacao = "Acima do peso"
else:
    classificacao = "Obeso"

print("Seu IMC é:", round(imc, 2))
print("Classificação:", classificacao)
