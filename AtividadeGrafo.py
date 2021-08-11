
#Funcoes
#criar matrix
def matriz():
    for i in range(vertices):
        Linha = []
        for j in range(vertices):
            Linha.append(0)
        grafo.append(Linha)


#imprimir matriz
def imprimir_matriz():
    for i in range(vertices):
        for j in range(vertices):
           print(grafo[i][j], end = " ")
        print("")


#adicionar arestas
def add_aresta(l, c, arestas):
    grafo[l-1][c-1] = arestas
    grafo[c-1][l-1] = arestas

#grau de cada vertice
def grau_vertice():
    grau = 0
    for i in range(vertices):
        for j in range(vertices):
            grau += grafo[i][j]

        print("O grau do vertice ", i+1, "eh ", grau)
        grau = 0
    
        
    

#grau minimo
def Min_grau():
    min_grau = 100
    grau = 0
    vertice = 0
    aux = 0

    for i in range(vertices):
        for j in range(vertices):
            grau += grafo[i][j]

        if(min_grau>grau):
             min_grau = grau
             vertice = i

        grau = 0  
    print("O grau minino eh do vertice ", vertice+1 , "com grau", min_grau)

#grau maximo
def Max_grau():

    max_grau = 0
    grau = 0
    vertice = 0
    aux = 0

    for i in range(vertices):
        for j in range(vertices):
            grau += grafo[i][j]

        if(max_grau<grau):
             max_grau = grau
             vertice = i

        grau = 0
    print("O grau maximo eh do vertice ", vertice+1 , "com grau", max_grau)

#inicio e chamada das funcoes

print('-------------| Grafo |--------------')
grafo = []
vertices = int (input("Quantidade de vertices do Grafo: "))

matriz()
imprimir_matriz()

resposta = 's'

print("--------| adicionando arestas |----------")
while resposta == 's':
    
    print('indique a linha e coluna e quantidade respectivamente')
    linha = int(input('Linha: '))
    coluna = int (input('Coluna: '))
    arestas = int(input('Quantidade: '))
    add_aresta(linha, coluna, arestas)
    resposta = input('Deseja adicionar arestas? [s/n]: ')


imprimir_matriz()

grau_vertice()

Min_grau()

Max_grau()




