# Uma loja está realizando um levantamento a respeito das pendências financeiras dos seus
# clientes. A ideia é levantar o percentual de clientes que se enquadram em cada uma das
# seguintes situações:
# • Clientes isentos de pendências
# • Clientes com parcelas em dia e
# • Clientes com parcelas em atraso.
# Para isto, desenvolva um programa que receba do usuário o número de clientes em cada uma
# destas situações, e retorne como saída para o usuário o percentual de clientes que se enquadra
# em cada uma das situações.

isentos = int(input('informe a quantidade de clientes isentos de pendencias: '))
emdia = int(input('informe a quantidade de clientes com parcelas em atraso: '))
atrasados = int(input('informe a quantidade de clientes com parcelas em atraso: '))

totaldecliente = isentos + emdia + atrasados

percentisentos = (isentos / totaldecliente) * 100
percentemdia = (emdia / totaldecliente) * 100
percentatrasados = (atrasados / totaldecliente) * 100

print(f' o percentual de clientes isentos de pendencias é de {percentisentos: .1f}% ')
print(f' o percentual de clientes com parcelas em dia é de {percentemdia: .1f}% ')
print(f' o percentual de clientes com parcelas em atraso é de {percentatrasados: .1f}% ')
