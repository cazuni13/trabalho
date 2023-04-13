# Sabe-se que para iluminar de maneira correta os cômodos de uma casa, para cada metro
# quadrado de área deve-se usar 18 watts de potência. Desenvolva um programa que receba as
# dimensões de dois lados de uma casa (em metros), calcule a área da casa (A = lado * lado), e
# mostre quantos watts serão necessários para iluminar corretamente esta casa

print('informe em metros o tamanho do lado frontal e do lado lateral da casa.')

ladolateral = float(input('informe o lado lateral: '))
ladofrontal = float(input('informe o lado frontal: '))

area = ladofrontal * ladolateral
watts = area * 18

print(f'sua casa tem uma área total de {area:.1f}m². para ilumina-la coretamente irá usar {watts:.1f} watts de potência')