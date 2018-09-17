import random

# f(d) = a*e^d - 4*d^2 | f'(d) = a*e^d - 8*d

# Globals
itv = [0,1] #intervalo
e = 2.71 #número de euler


def erros(x, xb):
    absoluto = abs(x-xb)
    relativo = abs(absoluto)/abs(xb)
    return (abs(absoluto),abs(relativo))


def mov(d, a):
    r = a*(e**d)-4*(d**2)
    return r


def bissecao(n, a, er):
    nitv = itv  #intervalo
    y = nitv[0] #inicio intervalo
    z = nitv[1] #fim intervalo
    k = 0       #cont iterações
	
	#verifica se há raíz entre a e b, o retornando se for o caso
    if(mov(y,a)*mov(z,a) >= 0):
        print("Não há raiz entre a e b")
        return 1
    elif(z-y<er):
        return (nitv, (y+z)/2)
    else:
        m = mov(y,a) #m recebe o valor de f(y)

    print('\n## Iterações | Ii = {}'.format(nitv))
    while(k < n):
        x = float((y+z)/2) 
        if(m*mov(x,a) > 0): #testa as condições para mudança do intervalo
            y = x
        else:
            z = x
        nitv = [y,z] 
        ErroRelativo = erros(z,y)
        print("I: {}\tRA(d{}): {}\tER: {}".format(nitv,k+1,y+ErroRelativo[1], ErroRelativo[1]))
        if((z-y)<er): #testa se intervalo é pequeno suficiente
            return (nitv,(y+z)/2) 
        k = k+1
    return (nitv,(y+z)/2)


def moveNR(d, a):
    new_d = d - mov(d,a)/(a*(e**d) - 8*d)
    return new_d


def newton_raphson(n, a, er):
    nitv = itv  #intervalo
    d = (nitv[1] - nitv[0])/2 #chute inicial
    k = 0 #cont iteração

    if(abs(moveNR(d,a)) < er):
        return (nitv,d)

    print('\n## Iterações | Ii = {}'.format(nitv))
    while(k < n):  
        f = moveNR(d, a) #valor da função
        nitv[0] = min(d,f) 
        nitv[1] = max(d,f)
        ErroRelativo = erros(f,d)
        print("I: {}\tRA(d{}): {}\tER: {}".format(nitv,k,d,abs(ErroRelativo[1])))
        if((abs(moveNR(f,a)) < er) or ((abs(f - d)) < er)):
            return (nitv,f) # d é a raiz aproximada moveNR(f,a)
        d = f
        k = k+1
    return (nitv,d)


def moveS(d, nd, a):
    new_d = nd - (mov(nd,a))*(nd-d)/((mov(nd,a)) - (mov(d,a)))
    return new_d
 

def secante(n, a, er):
    nitv = itv #intervalo
    d = (itv[1] - itv[0])/2 # d0
    nd = itv[1] # d1
    k = 0 #cont inicial

    if(abs(mov(d,a)) < er):
        return (nitv,d)
    if((abs(mov(nd,a)) < er) or (abs(nd-d) < er)):
        return (nitv,nd)

    print('\n## Iterações | Ii = {}'.format(nitv))
    while(k < n):
        f = moveS(d, nd, a) # d2
        nitv[0] = min(d,nd,f)
        nitv[1] = max(d,nd,f)
        ErroRelativo = erros(f,nd)
        print("I: {}\tRA(d{}): {}\tER(d{}): {}".format(nitv,k+1,nd,k+1,ErroRelativo[1]))
        if((abs(mov(f, a)) < er) or (abs(f-nd) < er)):
            return (nitv,nd)
        d = nd
        nd = f
        k = k+1
    return 0


def truncate(value, n):
    return int(value*(10**n))/(10**n)


def main():
    
    # Valores Iniciais
    n = int(input("Qtde de repetições(n): "))
    a = float(input("Amplitude(a): "))
    er = float(input("Precisão(er): ")) #ex.: 10^4 = 0.0001

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
        
    print('\n## Resultado\nIntervalo: {} | Raiz Aproximada: {}'.format(Resultado[0],truncate(Resultado[1],4)))


if __name__ == "__main__":
    main()
