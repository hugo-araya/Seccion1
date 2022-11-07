
def erro(n):
    global golbal
    print(golbal)
    golbal = golbal + 1
    if n == 0:
        return 1
    else:
        return erro(n+1)

if __name__ == "__main__":
    golbal = 1
    print(erro(50))
