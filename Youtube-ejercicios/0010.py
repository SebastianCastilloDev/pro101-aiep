# calcular n+ nn + nnn

n = input('ingrese n')

print('valor = ', int(n)+int(n*2)+int(n*3))
print('valor = ', int(n)+int(n+n)+int(n+n+n))

nn = int('{}{}'.format(n, n))
nnn = int('%s%s%s' % (n, n, n))

suma = int(n)+nn+nnn

print(suma)
