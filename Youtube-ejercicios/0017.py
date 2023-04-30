#  determinar si es cercano a 1000 o 2000

def cercania(n):
    return (abs(1000-n) < 100) or (abs(2000-n) < 100)


numero = int(input('ingresa un n: '))

if cercania(numero):
    print('el numero {} es cercano a 1000 o 2000'.format(numero))
else:
    print('naka la pirinaka')
