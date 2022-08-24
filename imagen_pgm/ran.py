import random
im = open('Image/dos.pgm','w')
im.write('P2\n')
im.write('# Hugo Araya Carrasco\n')
im.write('512 512\n')
im.write('255\n')
imagen = ''
for i in range(512*512):
    numero = random.randint(0,255)
    imagen = imagen + str(numero)+' '

im.write(imagen+'\n')
im.close()