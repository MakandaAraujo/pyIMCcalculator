print('Olá, vamos calcular seu IMC?')
altura = float(input('Pra isso vamos precisar de sua altura, digite por favor: '))
peso = float(input('Hmmm show, agora vamos pra seu peso: '))
imc = peso/(altura * altura)
print(f"esse é seu IMC {imc:.2f}" ) #Jeito Chei de munganga (simplificado seria: round(imc, 2))
if imc < 18.6:
    print('Você está abaixo do indice de magreza')
elif 18.6 <= imc < 24.9:
    print("Você está bem")
elif 25 <= imc < 29.9:
    print('Levemente acima do peso')
elif 30 <= imc < 34.9:
    print('Obesidade nivel 1')
elif 35 <= imc < 39.9:
    print('Obesidade nivel 2(severa)')
else:
    print('Obesidade nivel 3(mórbida)')


#Potenciação 3⁴ = 3**4
