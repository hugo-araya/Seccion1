im = open('Image/Lena_ascii.pgm')
magica = im.readline().rstrip('\n')
comentario = []
linea = im.readline().rstrip('\n')
while linea[0] == '#':
    comentario.append(linea)
    linea = im.readline().rstrip('\n')
sep = ' '
dimension = linea.split(sep)
ancho = int(dimension[0])
alto = int(dimension[2])
grises = int(im.readline().rstrip('\n'))

pixeles = []
for linea in im:
    linea = linea.rstrip('\n')
    lista = linea.split(' ')
    for pixel in lista:
        if pixel != '':
            pixeles.append(int(pixel))

# Binarizado

nueva = []
for pixel in pixeles:
    if pixel >= 128:
        nueva.append(255)
    else:
        nueva.append(0)

sal = open('Image/binaria1.pgm','w')
sal.write('P2\n')
sal.write('# by Hugo Araya Carrasco\n')
sal.write('512 512\n')
sal.write('255\n')
for pixel in nueva:
    sal.write(str(pixel)+' ')
sal.write('\n')
im.close()
sal.close()






