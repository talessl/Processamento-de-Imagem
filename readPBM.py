#utilizando imageio.v2, o branco se refere a true e o preto a false
import imageio.v2 as imageio

# Carrega a imagem binária
img = imageio.imread('c:\\Users\\tales\\Desktop\\Códigos\\Pyhton\\PI\\imagemGIMP2.0.pbm')

# verificando a forma (shape) da imagem
print(img.shape)  # (altura, largura)

matriz = []
for i in range(img.shape[0]):
    linha = []
    for j in range(img.shape[1]):
        if img[i][j] == 1:
            linha.append(0)
        
        if img[i][j] == 0:
            linha.append(1)
    matriz.append(linha)

print("Matriz:")
for linha in matriz:
    print(linha)
