#utilizando imageio.v2, o branco se refere a true e o preto a false
import imageio.v2 as imageio
import numpy as np

# Carrega a imagem binária
img = imageio.imread(r"c:\\Users\\tales\\Desktop\\Códigos\\Pyhton\\PI\\imagemGIMP2.0.pbm")


def leMatriz(img):
    matriz = []
    for i in range(img.shape[0]):
            linha = []
            for j in range(img.shape[1]):
                if img[i][j] == 1:
                 linha.append(0)
                if img[i][j] == 0:
                    linha.append(1)
                    
           
            matriz.append(linha)    
    """print("Matriz: ")
    for linha in matriz:
        for elemento in linha:
            print(elemento, end = " ")
        print("\n")	"""
    return matriz

def print_matrix(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print("\n")


"""def dilataMatriz3x3(matriz):
    matriz_dilatada = []
    
    for i in range(1, len(matriz) - 1):
        linha_dilatada = []
        for j in range(1, len(matriz[i]) - 1):
            if (matriz[i][j+1] == 1 or matriz[i+1][j] == 1 or matriz[i+1][j+1] == 1 or
                matriz[i][j-1] == 1 or matriz[i-1][j] == 1 or matriz[i-1][j-1] == 1 or
                matriz[i-1][j+1] == 1 or matriz[i+1][j-1] == 1 or matriz[i][j] == 1):
                linha_dilatada.append(1)
            else:
                linha_dilatada.append(0)
                
        matriz_dilatada.append(linha_dilatada)

    print("Matriz dilatada: ")
    for i in range(len(matriz_dilatada)):
        for j in range(len(matriz_dilatada[i])):
            print(matriz_dilatada[i][j], end = " ")
        print("\n")
    """

def complemento(matriz):
    matriz_complemento = []
    for i in range(len(matriz)):
        linha_complemento = []
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1:
                linha_complemento.append(0)
            else:
                linha_complemento.append(1)
        matriz_complemento.append(linha_complemento)
    print("Matriz complemento: ")
    for i in range(len(matriz_complemento)):
        for j in range(len(matriz_complemento[i])):
            print(matriz_complemento[i][j], end = " ")
        print("\n")
    return matriz_complemento


def interseccao(matriz1, matriz2):
    matriz_interseccao = []
    for i in range(len(matriz1)):
        linha_interseccao = []
        for j in range(len(matriz1[i])):
            if matriz1[i][j] == 1 and matriz2[i][j] == 1:
                linha_interseccao.append(1)
            else:
                linha_interseccao.append(0)
        matriz_interseccao.append(linha_interseccao)
    print("Matriz interseccao: ")
    for i in range(len(matriz_interseccao)):
        for j in range(len(matriz_interseccao[i])):
            print(matriz_interseccao[i][j], end = " ")
        print("\n")
    return matriz_interseccao


def main():
    leMatriz(img)
    return 0

if __name__ == '__main__':
    main()
    print_matrix(leMatriz(img))
    #dilataMatriz3x3(leMatriz(img))
    #complemento(leMatriz(img))

