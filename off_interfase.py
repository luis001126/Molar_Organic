print('calcaular las masa molar de cualquier sustancia organica')

C = 12
H = 1
O = 16
N = 32
S = 17
Na = 11

def Calculo1(result1):
    result1: int = (car1 * C) + (hidro1 * H)
    return result1
def Calculo2(result2):
    result2: int = (car2 * C) + (hidro2 * H) + (oxi2*O)
    return result2
def Calculo3(result3):
    result3: int = (car3 * C) + (hidro3 * H) + (oxi3 * O) + (nitro3 * N)
    return result3

print('Seleccione de las siguintes variantes cual se corresponde')
print('1.CH    2.CHO    3.CHON    4.CHONS    5.CHONSNa')
valor = int(input('Seleccion: '))
if 5 < valor or valor < 1:
    print('error')
else:
    if valor == 1:
        car1 = int(input('cantidad de carbonos: '))
        hidro1 = int(input('cantidad de hidrogenos: '))
        name1 = f'C{car1}H{hidro1}'
        print(f'La masa molar del {name1} es {Calculo1(result1='')}')

    elif valor == 2:
        car2 = int(input('cantidad de carbonos: '))
        hidro2 = int(input('cantidad de hidrogenos: '))
        oxi2 = int(input('cantidad de oxigeno: '))
        name2 = f'C{car2}H{hidro2}O{oxi2}'
        print(f'La masa molar del {name2} es {Calculo2(result2='')}')

    elif valor== 3:
        car3 = int(input('cantidad de carbonos: '))
        hidro3 = int(input('cantidad de hidrogenos: '))
        oxi3 = int(input('cantidad de oxigeno: '))
        nitro3 = int(input('cantidad de nitrogeno: '))
        name3 = f'C{car3}H{hidro3}O{oxi3}N{nitro3}'
        print(f'La masa molar del {name3} es {Calculo3(result3='')}')