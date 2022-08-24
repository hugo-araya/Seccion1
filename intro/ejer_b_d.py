nrob = input('Binario: ')
ok = True
while len(nrob) !=8 and ok != False:
    for dig in nrob:
        if dig != "0" and dig != "1":
            ok = False
    print("Error digitacion, por favor reingresar.")
    nrob = input('Binario: ')

i = 0
nrod = 0
L = len(nrob)-1
while i < len(nrob):
    nrod = nrod + int(nrob[i])*2**(L-i)
    i = i+1
print(nrod)
