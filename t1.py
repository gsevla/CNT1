# f(d) = a*e^d - 4*d^2

# Globals
itv = [0,1] # intervalo
e = 2.71 # número de euler


def movB(d, a):
    r = a*(e**d)-4*(d**2)
    return r


def bissecao(n, a, er):
    nitv = itv
    y = nitv[0]
    z = nitv[1]
    k = 0
    if(movB(y,a)*movB(z,a) >= 0):
        return "ERRO"
    elif((z-y)<10**(-er)):
        print('a1')
        return ((y,z),y+(z-y))
    else:
        m = movB(y,a)

    print('\n## Iterações | Ii = {}'.format(nitv))
    while(k < n):
        x = float((y+z)/2)
        if(m*movB(x,a) > 0):
            y = x
        else:
            z = x
        nitv = [y,z]
        
        ErroRelativo = z-y
        print("I: {}\tRA: {}\tER: {}".format(nitv,y+ErroRelativo, ErroRelativo))
        if((z-y)<10**(-er)):
            return (nitv,y+ErroRelativo)
        k = k+1
    return (nitv,y+ErroRelativo)


def moveNR(d, a):
    new_d = d - (a*(e**d) - 4*(d**2))/(a*(e**d) - 8*d)
    return new_d


def newton_raphson(n, a, er):
    d = (itv[1] - itv[0])/2
    k = 0
    nitv = itv

    if(abs(moveNR(d,a)) < 10**(-er)):
        return (nitv,d)

    print('\n## Iterações | Ii = {}'.format(nitv))
    while(k < n):  
        f = moveNR(d, a)
        nitv[0] = min(d,f)
        nitv[1] = max(d,f)
        ErroRelativo = abs(abs(f-d)/abs(d))
        print("I: {}\tRA(d{}): {}\tER: {}".format(nitv,k,d,abs(ErroRelativo)))

        if((abs(moveNR(f,a)) < 10**(-er)) or ((abs(f - d)) < 10**(-er))):
            return (nitv,moveNR(f,a)) # d é a raiz aproximada
        d = f
        k = k+1
    return (nitv,d)


def moveS(d, nd, a):
    new_d = nd - (a*(e**nd) - 4*(nd**2))*(nd-d)/((a*(e**nd) - 4*(nd**2)) - (a*(e**d) - 4*(d**2)))
    return new_d
 

def secante(n, a, er):
    d = (itv[1] - itv[0])/2 # d0
    nd = itv[1] # d1
    k = 0
    nitv = itv

    if(abs((a*e**d) - (4*d**2)) < 10**(-er)):
        return (nitv,d)
    if((abs((a*e**nd) - (4*nd**2)) < 10**(-er)) or (abs(nd-d) < 10**(-er))):
        return (nitv,nd)

    print('\n## Iterações | Ii = {}'.format(nitv))
    while(k < n):
        f = moveS(d, nd, a) # d2
        nitv[0] = min(d,nd,f)
        nitv[1] = max(d,nd,f)

        #ErroRelativod = abs(abs(nd-d)/abs(d))
        ErroRelativond = abs(abs(f-nd)/abs(nd))
        print("I: {}\tRA(d{}): {}\tER(d{}): {}".format(nitv,k+1,nd,k+1,ErroRelativond))
        if((abs((a*e**f) - (4*f**2)) < 10**(-er)) or (abs(f-nd) < 10**(-er))): 
            return (nitv,nd)
        d = nd
        nd = f
        k = k+1
    return 0


def main():
    n = int(input("Qtde de repetições(n): "))
    a = float(input("Amplitude(a): "))
    er = float(input("Precisão(er): "))

    # GUI
    print("\n## Métodos")
    print("0. Sair")
    print("1. Bisseção")
    print("2. Newton-Raphson")
    print("3. Secante")
    op = input("Opção: ")

    while((op != '0') and (op != '1') and (op != '2') and (op != '3')):
        print('Digite uma opção válida! (0. Sair)')
        op = input("Opção: ")
        if(op == '0'):
            break
    if(op == '1'):
        Resultado = bissecao(n, a, er)
    elif(op == '2'):
        Resultado = newton_raphson(n, a, er)
    elif(op == '3'):
        Resultado = secante(n, a, er)
    else:
        print('\nAté a próxima!')
        return 0
        

    print('\n## Resultado\nIntervalo: {} | Raiz Aproximada: {}'.format(Resultado[0],Resultado[1]))


if __name__ == "__main__":
    main()
