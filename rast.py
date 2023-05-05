
def dilatar(matriz):
    eixoX = len(matriz)
    eixoY = len(matriz[0])
    val_x_max = eixoX-1
    val_y_max = eixoY-1

    img_dilatada = [[0 for _ in range(eixoY)] for _ in range(eixoX)]

    for i in range(eixoX):
        for j in range(eixoY):
            #canto superior esquerdo
            if(i == 0 and j == 0):
                if(matriz[i][j] == 1 or matriz[i][j+1] == 1 or 
                    matriz[i+1][j] == 1 or matriz[i+1][j+1] == 1):
                    img_dilatada[i][j] = 1
            #canto superior direito
            elif(i == 0 and j ==val_y_max):
                if(matriz[i][j-1] == 1 or matriz[i][j] == 1 or 
                    matriz[i+1][j-1] == 1 or matriz[i+1][j] == 1):
                    img_dilatada[i][j] = 1
            #canto inferior esquerdo
            elif(i == val_x_max and j == 0):
                if(matriz[i-1][j] == 1 or matriz[i-1][j+1] == 1 or 
                    matriz[i][j] == 1 or matriz[i][j+1] == 1):
                    img_dilatada[i][j] = 1
            #canto inferior direito
            elif(i == val_x_max and j == val_y_max):
                if(matriz[i-1][j-1] == 1 or matriz[i-1][j] == 1 or 
                    matriz[i][j-1] == 1 or matriz[i][j] == 1):
                    img_dilatada[i][j] = 1
            #lateral esquerda
            elif(j == 0):
                if(matriz[i-1][j] == 1 or matriz[i-1][j+1] == 1 or 
                    matriz[i][j] == 1 or matriz[i][j+1] == 1 or 
                    matriz[i+1][j] == 1 or matriz[i+1][j+1] == 1):
                    img_dilatada[i][j] = 1
            #teto
            elif(i == 0):
                if(matriz[i][j-1] == 1 or matriz[i][j] == 1 or matriz[i][j+1] == 1 or 
                    matriz[i+1][j-1] == 1 or matriz[i+1][j] == 1 or matriz[i+1][j+1] == 1):
                    img_dilatada[i][j] = 1
            #lateral direita
            elif(j == val_y_max):
                if(matriz[i-1][j-1] == 1 or matriz[i-1][j] == 1 or 
                    matriz[i][j-1] == 1 or matriz[i][j] == 1 or 
                    matriz[i+1][j-1] == 1 or matriz[i+1][j] == 1):
                    img_dilatada[i][j] = 1
            #chao
            elif(i == val_x_max):
                if(matriz[i-1][j-1] == 1 or matriz[i-1][j] == 1 or matriz[i-1][j+1] == 1 or 
                    matriz[i][j-1] == 1 or matriz[i][j] == 1 or matriz[i][j+1] == 1):
                    img_dilatada[i][j] = 1
            #default
            else:
                if(matriz[i-1][j-1] == 1 or matriz[i-1][j] == 1 or matriz[i-1][j+1] == 1 or 
                    matriz[i][j-1] == 1 or matriz[i][j] == 1 or matriz[i][j+1] == 1 or 
                    matriz[i+1][j-1] == 1 or matriz[i+1][j] == 1 or matriz[i+1][j+1] == 1):
                    img_dilatada[i][j] = 1

    return img_dilatada

#abrindon as duas imagens,  a já existente e a nova imagem sendo criada
imagem = open("imagemteste.pbm").readlines()
nova_imgem = open("nova_imagem.pbm",'w')
nova_imgem_2 = open("nova_imagem_2.pbm",'w')

#as 3 primeiras linhas são iguais em ambas imagens
for linha in range(2):
    nova_imgem.write(imagem[linha])
    nova_imgem_2.write(imagem[linha])


#retirando as dimensões da linha
dimensions = [eval(i) for i in imagem[2].strip().split(' ')]
axisX = dimensions[0]+1
axisY = dimensions[1]+1

nova_imgem.write(str(axisX+1) + ' ' + str(axisY+1) + '\n')
nova_imgem_2.write(str(axisX+1) + ' ' + str(axisY+1) + '\n')


nova_img = [[0 for _ in range(axisY+1)] for _ in range(axisX+1)]
del imagem[0:3]

imagem = ''.join([s.rstrip() for s in imagem])
i = 1
j = 1

#salvando numa matriz
for x in range(len(imagem)):
    if((x%(dimensions[0])== 0 ) and x != 0):
        i += 1
        j = 1

    pixel = imagem[x]
    nova_img[i][j] = int(pixel)
    j+=1

for x in range(len(nova_img)):
    for y in range(len(nova_img[x])):
        nova_imgem_2.write(str(nova_img[x][y]))
    nova_imgem_2.write('\n')

nova_img = dilatar(nova_img)

#salvando em novo arquivo
for x in range(len(nova_img)):
    for y in range(len(nova_img[x])):
        nova_imgem.write(str(nova_img[x][y]))
    nova_imgem.write('\n')

nova_imgem.close()
nova_imgem_2.close()
