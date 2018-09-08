# f(d) = a*e^d - 4*d^2

# Globals
itv = [0,1] # intervalo
e = 2.71 # número de euler


def moveNR(d, a):
    new_d = d - (a*(e**d) - 4*(d**2))/(a*(e**d) - 8*d)
    return new_d


def newton_raphson(n, a, er):
    d = (itv[1] - itv[0])/2
    k = 0
    nitv = itv

    while(k < n):
        nitv[0] = d      
        f = moveNR(d, a)
        nitv[1] = f
        ErroRelativo = abs((f-d))/abs(d)
        print("I: {}\tRA: {}\tER: {}".format(nitv,d,abs(ErroRelativo)))

        if((abs(f) < 10**(-er)) or ((abs(f - d)) < 10**(-er))):
            return d # d é a raiz aproximada
        d = f
        k = k+1


def moveS(d, nd, a):
    new_d = nd - (a*(e**nd) - 4*(nd**2))*(nd-d)/((a*(e**nd) - 4*(nd**2)) - (a*(e**d) - 4*(d**2)))
    return new_d


def secante(n, a, er):
    d = (itv[1] - itv[0])/2
    nd = itv[1]
    k = 0
    nitv = itv

    while(k < n):
        nitv[0] = d
        f = moveS(d, nd, a)
        nf = moveS(nd, f, a)
        ErroRelativod = abs((f-d))/abs(d)
        ErroRelativond = abs((nf-f))/abs(f)
        print("I: {}\tRA(d{}): {}\tER(d{}): {}\tRA(d{}): {}\tER(d{}): {}".format(nitv,k,d,k+1,abs(ErroRelativod),nd,k+1,k+2,abs(ErroRelativond)))
        nitv[1] = f
        if((abs(f) < 10**(-er)) or (abs(nd-d) < 10**(-er))): 
            return nd
        elif((abs(nf) < 10**(-er)) or (abs(nf-f) < 10**(-er))):
            return f
        d = nd
        nd = f
        k = k+1


def main():
    n = int(input("Qtde de repetições(n): "))
    a = float(input("Amplitude(a): "))
    er = float(input("Precisão(er): "))

    #RaizAproximada = newton_raphson(n, a, er)
    RaizAproximada = secante(n, a, er)
    print('Raiz Aproximada: {}\n'.format(RaizAproximada))


if __name__ == "__main__":
    main()