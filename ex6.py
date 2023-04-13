# Suponha que um caixa disponha apenas de cédulas de R$ 100, 10 e 1. Escreva um programa
# para ler o valor de uma conta e o valor fornecido pelo usuário para pagar essa conta, e calcule e
# troco. Calcular e mostrar a quantidade de cada tipo de cédula que o caixa deve fornecer como
# troco. Mostrar, também o valor da compra e do troco.

conta = float(input("Digite o valor da conta: R$"))
pago = float(input("Digite o valor pago pelo cliente: R$"))

troco = pago - conta

notacem = int(troco / 100)
troco = troco % 100
notadez = int(troco / 10)
troco = troco % 10
notaum = int(troco)

print(f'Valor da compra é de R${conta:.2f} e o valor pago é de R${pago:.2f}')
print(f' o Troco foi de R${(pago - conta):.2f} e sairam {notacem} cédulas de R$100, {notadez} cédulas de R$10 e {notaum} cédulas de R$1')
