# f(d) = a*e^d - 4*d^2

# Globals
itv = [0,1] # intervalo
e = 2.71 # número de euler


def move(d, a):
    new_d = d - (a*(e**d) - 4*(d**2))/(a*(e**d) - 8*d)
    return new_d


def newton_raphson(n, a, er):
    d = (itv[1] - itv[0])/2
    k = 0

    while(k < n):
        itv[0] = d      
        f = move(d, a)
        itv[1] = f
        ErroRelativo = abs((f-d))-abs(d)
        print("I: {}\tRA: {}\tER: {}".format(itv,d,abs(ErroRelativo)))

        if((abs(f) < 10**(-er)) or ((abs(f - d)) < 10**(-er))):
            return d # d é a raiz aproximada
        d = f
        k = k+1


def main():
    n = int(input("Qtde de repetições(n): "))
    a = float(input("Amplitude(a): "))
    er = float(input("Precisão(er): "))

    RaizAproximada = newton_raphson(n, a, er)
    print('Raiz Aproximada: {}\n'.format(RaizAproximada))


if __name__ == "__main__":
    main()