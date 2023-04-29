# si tiene .py lo deja igual, si no le pone .py

def extension(name):

    if name[-3:] == '.py':
        return name
    else:
        return name + '.py'


print(extension('main.py'))
print(extension('main'))
