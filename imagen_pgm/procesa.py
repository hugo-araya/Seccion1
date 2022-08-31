import ImagenPGM as im

if __name__ == '__main__':
#   nombre = input('nombre de archivo: ')
    nombre = 'Lena_ascii'
    nombre = nombre + '.pgm'
    imagen1 = im.LeerImagen(nombre)
    imagen2 = im.Binariza(imagen1)
    imagen3 = im.Negativo(imagen1)
    imagen4 = im.Negativo(imagen2)
    im.EscribirImagen('binarizada1.pgm', imagen2)
    im.EscribirImagen('negativo1.pgm', imagen3)
    im.EscribirImagen('negativodelbinario1.pgm', imagen4)
    imagen2 = im.LeerImagen('binarizada1.pgm')
    imagen3 = im.LeerImagen('negativo1.pgm')
    imagen4 = im.LeerImagen('negativodelbinario1.pgm')
    im.Informacion(imagen1)
    im.Informacion(imagen2)
    im.Informacion(imagen3)
    im.Informacion(imagen4)
