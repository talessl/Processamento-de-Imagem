from scipy import ndimage
import numpy as np
import imageio.v2 as imageio

# Carrega a imagem binária
img = imageio.imread('c:\\Users\\tales\\Desktop\\Códigos\\Pyhton\\PI\\imagemTest3.0.png', mode='L')

# Define o tamanho do kernel de dilatação
kernel_size = 2

# Define o kernel de dilatação como um quadrado
kernel = np.zeros((kernel_size, kernel_size), dtype=bool)

# Aplica a dilatação binária na imagem
dilated = ndimage.binary_dilation(img, structure=kernel)

# Subtrai a imagem dilatada da imagem original
result = dilated - img

# Salva a imagem resultante
imageio.imsave('imagemTeste3.0Dilatada.png', result)
