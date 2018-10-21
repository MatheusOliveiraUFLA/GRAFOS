def constroi_matriz(QtdVertices):
    linha = QtdVertices
    coluna= QtdVertices
    #só pra ficar mais entendível, escrevi linha e coluna
    return [[0] * linha for i in range(coluna)]

def main():
    QtdVertices = int(input("Insira a quantidade de vértices:"))
    matriz = constroi_matriz(QtdVertices)
    
    #inserindo as arestas
    #um vértice pode se ligar a quaisquer outro do grafo, porém o exercício deixa claro a utilização de um grafo acíclico
    for i in range(0,(QtdVertices)):
        j=0
        while(j<(QtdVertices)):
            if(i==j and j != QtdVertices-1):
                j= j+1
            
            if(i==QtdVertices-1 and j==QtdVertices):
                entrada = "n"
            else:
                entrada = input("O vertice {0} tem ligação com o vértice {1}? (s/n)".format(i+1, j+1))
            
            if entrada is "s":
                matriz[i][j] = 1
            j = j+1
        print()

    #cria lista com os valores inicialmente nulos
    antecessores = [[] * QtdVertices for i in range(QtdVertices)]
    
    #começando o percurso sempre do primeiro vértice
    percurso = [1]

    #insere os antecessores de cada vértice
    for i in range(QtdVertices):
        j=0
        while(j<(QtdVertices)):
            if(i==j and j != QtdVertices-1):
                j= j+1
            if matriz[i][j] == 1:
                antecessores[j].append(i+1)
            j+=1

    #o percurso só avança pra um vértice se todos os antecessores já estão na lista de percurso.
    for w in range(QtdVertices):
        for i in range(QtdVertices):
            j=0
            while(j<(QtdVertices)):
                if(i==j and j != QtdVertices-1):
                    j= j+1

                a = set(antecessores[j]).difference(percurso)
                b = j+1 in percurso
                if(matriz[i][j]==1 and not a and not b):
                    percurso.append(j+1)
                j+=1
    
    if(not set(percurso).difference(range(QtdVertices))):
        print("Solução não encontrada!")
    else:
        print ("Solução Encontrada!")
        print("Ordem de visitação das atividades:" ,percurso)



main()