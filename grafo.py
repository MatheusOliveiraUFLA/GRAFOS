def verificaGrafo(matriz,lista):
    eureliano = True
    cont = 0
    lista = []
    somaGraus = 0 
    for a in range(0,7):
        somaGraus += cont
        lista.insert(a-1,cont)
        if(cont%2 != 0):
            print (a)
            eureliano = False
        cont = 0 
        for b in range(0,7):
            cont += matriz[a][b]
            if(a==b and matriz[a][b] == 1):
                cont= cont + 1       
    return lista, eureliano, somaGraus
    
def cicloEuleriano(matriz,lista,somaGraus,ciclo,resultado,i): 
    linha = 0
    while(lista[i] == 0):
        i+=1
    linha = i
    ciclo.append(linha)
    coluna = 0
    while(coluna < 7):
        if(matriz[linha][coluna] == 1):
            ciclo.append(coluna)
            matriz[linha][coluna] = 0
            matriz[coluna][linha] = 0
            lista[linha] -= 1
            lista[coluna] -= 1
            somaGraus -= 2
            linha = coluna
            coluna = -1
            if(ciclo[0] == ciclo[len(ciclo)-1]):
                resposta = sequencia(matriz,lista,ciclo,resultado,somaGraus)
        coluna += 1
    return resposta
            
def sequencia(matriz,lista,ciclo,resultado,somaGraus):
    penultima = 0
    ultima = 0
    if(len(resultado) == 0 ):
        resultado = ciclo
        ultima = resultado[len(resultado)-1]
        penultima = resultado[len(resultado)-2]
        if(somaGraus):
            resultado.pop(len(resultado)-1)
            resultado.pop(len(resultado)-1)
        resultado.append(ultima)
    else:
        ultima = resultado[len(resultado)-1]
        penultima = resultado[len(resultado)-2]
        resultado.pop(len(resultado)-1)
        if(somaGraus):
            resultado.pop(len(resultado)-1)
        resultado.extend(ciclo)
        resultado.append(ultima)

    if(somaGraus != 0):
        ciclo = []
        cicloEuleriano(matriz,lista,somaGraus,ciclo,resultado,penultima)    
    return resultado

def main():
    matrizAdjacencia = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    qnt = int(input())
    grauVertices = []
    ciclo = []
    resultado = []
    somaGraus = 0
    for i in range(0,qnt):
        l,c = input().split()
        l = int(l)
        c = int(c)
        matrizAdjacencia[l][c] = 1
        matrizAdjacencia[c][l] = 1
    grauVertices, euleriano, somaGraus = verificaGrafo(matrizAdjacencia,grauVertices)
    if(euleriano):
        resultado = cicloEuleriano(matrizAdjacencia,grauVertices,somaGraus,ciclo,resultado,0)
        print('Sequência de peças: ')
        if(len(resultado)%2 == 0):
            for a in range(0, len(resultado)-1):
                print(resultado[a], "-",resultado[a+1])
        else:
            for a in range(0, len(resultado)-2):
                print(resultado[a], "-",resultado[a+1])
    else:
        print('A solução não pode ser encontrada')
main()

       
                    






