# Considere que para um consórcio sabe-se o número total de prestações, a quantidade de
# prestações pagas e o valor da prestação. Escreva um programa que determine o valor total pago
# pelo consorciado e o saldo devedor

totaldeprestacao = float(input('informe as prestações do consórcio: '))
valordaprestacao = float(input('informe o valor de cada prestação: '))
prestacaopaga = int(input('informe quantas prestações foram pagas: '))

totalpago = valordaprestacao * prestacaopaga
prestacaorestantes = totaldeprestacao - prestacaopaga
saldodevedor = prestacaorestantes * valordaprestacao

print(f'o valor ja pago pelo consórcio é de R${totalpago: .2f}, mas ainda restam R${saldodevedor: .2f} a serem pagos')
