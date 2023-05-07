def comparar_matrizes(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return False

    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            if matriz1[i][j] != matriz2[i][j]:
                return False

    return True

def copia_matriz(matriz):
    copia = [[0 for _ in range(len(matriz[0]))] for _ in range(len(matriz))]

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            copia[i][j] = matriz[i][j]

    return copia

def unir_imagem(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return False

    img_unida = [[0 for _ in range(len(matriz1[0]))] for _ in range(len(matriz1))]

    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            if matriz1[i][j] == 1 or matriz2[i][j] == 1:
                img_unida[i][j] = 1

    return img_unida

#operações morfológicas
#aplicação da dilatação em uma matriz de entrada e comparando com a matriz original
def dilatar_componente(matriz_entrada, matriz_original):
    eixoX = len(matriz_entrada)
    eixoY = len(matriz_entrada[0])

    img_dilatada = [[0 for _ in range(eixoY)] for _ in range(eixoX)]

    for i in range(1,eixoX-1):
        for j in range(1,eixoY-1):
            if(matriz_entrada[i-1][j-1] == 1 or matriz_entrada[i-1][j] == 1 or matriz_entrada[i-1][j+1] == 1 or 
               matriz_entrada[i][j-1] == 1 or matriz_entrada[i][j] == 1 or matriz_entrada[i][j+1] == 1 or 
               matriz_entrada[i+1][j-1] == 1 or matriz_entrada[i+1][j] == 1 or matriz_entrada[i+1][j+1] == 1):
                if(matriz_original[i][j] == 1):
                    img_dilatada[i][j] = 1

    return img_dilatada
#aplicação de dilaatação em uma imagem que começou com um pixel apenas e vai crescendo até preencher o objeto
def extracao_de_compenentes_isolado_continuacao(matriz_anterior, matriz_original):
    img_dilatada = dilatar_componente(matriz_anterior, matriz_original) 
    if(comparar_matrizes(matriz_anterior, img_dilatada)):
        return matriz_anterior
    else:
        return extracao_de_compenentes_isolado_continuacao(img_dilatada, matriz_original)
#aplicação de dilaatação em uma matriz criada totalmente branca, a ideia disso é armazenar o objeto em uma matriz isolado dos outros objetos
def extracao_de_compenentes_isolado_inicio(matriz_original, posicao_x,posicao_y):
    eixoX = len(matriz_original)
    eixoY = len(matriz_original[0])
    i = posicao_x
    j = posicao_y
    img_dilatada = [[0 for _ in range(eixoY)] for _ in range(eixoX)]

    img_dilatada[i][j] = 1
    img_dilatada = dilatar_componente(img_dilatada,matriz_original)

    return extracao_de_compenentes_isolado_continuacao(img_dilatada, matriz_original)

#preenchimento exterior da imagem
def dilatar_preenchimento(matriz,matriz_original):
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
                   matriz[i+1][j] == 1):
                    if(matriz_original[i][j] != 1): #diferente de 1 pq é o complemento, já que não é ideal pegar o negativo, que seria mto complexo, então sabemos que só retorna true no 0 ou seja no complemento
                        img_dilatada[i][j] = 1
            #canto superior direito
            elif(i == 0 and j ==val_y_max):
                if(matriz[i][j-1] == 1 or matriz[i][j] == 1 or 
                                          matriz[i+1][j] == 1):
                    if(matriz_original[i][j] != 1):
                        img_dilatada[i][j] = 1
            #canto inferior esquerdo
            elif(i == val_x_max and j == 0):
                if(matriz[i-1][j] == 1 or
                    matriz[i][j] == 1 or matriz[i][j+1] == 1):
                    if(matriz_original[i][j] != 1):
                        img_dilatada[i][j] = 1
            #canto inferior direito
            elif(i == val_x_max and j == val_y_max):
                if(                        matriz[i-1][j] == 1 or 
                    matriz[i][j-1] == 1 or matriz[i][j] == 1):
                    if(matriz_original[i][j] != 1):
                        img_dilatada[i][j] = 1
            #lateral esquerda
            elif(j == 0):
                if(matriz[i-1][j] == 1 or
                    matriz[i][j] == 1 or matriz[i][j+1] == 1 or 
                    matriz[i+1][j] == 1):
                    if(matriz_original[i][j] != 1):
                        img_dilatada[i][j] = 1
            #teto
            elif(i == 0):
                if(matriz[i][j-1] == 1 or matriz[i][j] == 1 or matriz[i][j+1] == 1 or 
                                          matriz[i+1][j] == 1):
                    if(matriz_original[i][j] != 1):
                        img_dilatada[i][j] = 1
            #lateral direita
            elif(j == val_y_max):
                if(                       matriz[i-1][j] == 1 or 
                   matriz[i][j-1] == 1 or matriz[i][j] == 1 or 
                                          matriz[i+1][j] == 1):
                    if(matriz_original[i][j] != 1):
                        img_dilatada[i][j] = 1
            #chao
            elif(i == val_x_max):
                if(                        matriz[i-1][j] == 1 or 
                    matriz[i][j-1] == 1 or matriz[i][j] == 1 or matriz[i][j+1] == 1):
                    if(matriz_original[i][j] != 1):
                        img_dilatada[i][j] = 1
            #default
            else:
                if(                        matriz[i-1][j] == 1 or
                    matriz[i][j-1] == 1 or matriz[i][j] == 1 or matriz[i][j+1] == 1 or 
                                           matriz[i+1][j] == 1):    
                    if(matriz_original[i][j] != 1):
                        img_dilatada[i][j] = 1

    return img_dilatada
#chamada de preenchimento_de_regiao
def preenchimento_de_regiao(matriz_anterior, matriz_original):
    eixoX = len(matriz_anterior)
    eixoY = len(matriz_anterior[0])

    imagem_preenchida = dilatar_preenchimento(matriz_anterior,matriz_original)

    if(comparar_matrizes(imagem_preenchida,matriz_anterior)):
        imagem_preenchida = unir_imagem(imagem_preenchida,matriz_original)
        return imagem_preenchida
    else:
        return preenchimento_de_regiao(imagem_preenchida,matriz_original)

#função que preenche buracos na imagem de modo recursivo, não exatamente igual a uma operação vista em sala, mas baseado em uma
def preenche_buraco(matriz,posicao_x,posicao_y):
    i = posicao_x
    j = posicao_y
    matriz[i][j] = 1

    if(matriz[i-1][j] == 0):
        matriz = preenche_buraco(matriz,i-1,j)
    if(matriz[i][j-1] == 0):
        matriz = preenche_buraco(matriz,i,j-1)
    if(matriz[i][j+1] == 0):
        matriz = preenche_buraco(matriz,i,j+1)
    if(matriz[i+1][j] == 0):
        matriz = preenche_buraco(matriz,i+1,j)

    return matriz
#função que procura buracos na imagem e retorna a quantidade de buracos e a posição de cada buraco além de preencher os buracos     
def procura_buraco(matriz):
    eixoX = len(matriz)
    eixoY = len(matriz[0])
    info_buraco = [0,[]]
    
    for i in range(eixoX):
        for j in range(eixoY):
            if(matriz[i][j] == 0):
                info_buraco[0] += 1
                info_buraco[1].append([i-1,j-1])
                preenche_buraco(matriz,i,j)

    return info_buraco
#função que preenche os objetos com pontos brancos
def preenche_objeto(matriz,posicao_x,posicao_y):
    i = posicao_x
    j = posicao_y
    matriz[i][j] = 0

    if(matriz[i-1][j-1] == 1):
        matriz = preenche_objeto(matriz,i-1,j-1)
    if(matriz[i-1][j] == 1):
        matriz = preenche_objeto(matriz,i-1,j)
    if(matriz[i-1][j+1] == 1):
        matriz = preenche_objeto(matriz,i-1,j+1)
    if(matriz[i][j-1] == 1):
        matriz = preenche_objeto(matriz,i,j-1)
    if(matriz[i][j+1] == 1):
        matriz = preenche_objeto(matriz,i,j+1)
    if(matriz[i+1][j-1] == 1):
        matriz = preenche_objeto(matriz,i+1,j-1)
    if(matriz[i+1][j] == 1):
        matriz = preenche_objeto(matriz,i+1,j)
    if(matriz[i+1][j+1] == 1):
        matriz = preenche_objeto(matriz,i+1,j+1)

    return matriz
#função que procura buracos na imagem e retorna a quantidade de buracos e a posição de cada buraco além de preencher os buracos     
def procura_objetos(matriz):
    eixoX = len(matriz)
    eixoY = len(matriz[0])
    info_objetos = [0,[],[],[]] # [quantidade de objetos, posição de cada objeto, [objeto(primeiro,segundo,...), quantidade de buracos], posição de cada buraco da imagem]  
    
    for i in range(eixoX):
        for j in range(eixoY):
            if(matriz[i][j] == 1):
                info_objetos[0] += 1
                info_objetos[1].append([i-1,j-1])

                img_inicial = [[0 for _ in range(axisY)] for _ in range(axisX)]
                img_inicial[0][0] = 1 #pixel inicial
                objeto_extraido = extracao_de_compenentes_isolado_inicio(matriz,i,j)
                objeto_extraido = preenchimento_de_regiao(img_inicial,objeto_extraido)

                info_buraco = procura_buraco(objeto_extraido)
                info_objetos[2].append([info_objetos[0],info_buraco[0]])
                if(info_buraco[0] != 0):
                    info_objetos[3].append(info_buraco[1])
                preenche_objeto(matriz,i,j)

    return info_objetos

#Organização de abertura e retirada da imagem para análise ###############################
#abrindo as duas imagens,  a já existente e a nova imagem sendo criada
imagem_recebida = input("Digite o nome da imagem a ser analisada: ")
imagem = open(imagem_recebida+".pbm").readlines()


#retirando as dimensões da linha
dimensions = [eval(i) for i in imagem[2].strip().split(' ')]
axisX = dimensions[0]+2
axisY = dimensions[1]+2

nova_img = [[0 for _ in range(axisY)] for _ in range(axisX)]
del imagem[0:3]

imagem = ''.join([s.rstrip() for s in imagem])
i = 1
j = 1
##########################################################################################

#salvando numa matriz e manipulando as imagens, salvando em uma imagem nova separada, a imagem com a borda
for x in range(len(imagem)):
    if((x%(dimensions[0])== 0 ) and x != 0):
        i += 1
        j = 1

    pixel = imagem[x]
    nova_img[i][j] = int(pixel)
    j+=1

#aplicação do trabalho
objetos = procura_objetos(nova_img)
#prints pedidos
print('Quantidade de objetos:',objetos[0])
#contando buracos
qtd_buracos = 0
for i in range(len(objetos[3])):
    qtd_buracos += len(objetos[3][i])

print('Quantidade de buracos totais:', qtd_buracos)
print('Quantidade de buracos de cada objeto:')
for i in range(len(objetos[2])):
    print('posição:',objetos[1][i], 'objeto',objetos[2][i][0],':',objetos[2][i][1])  
print('Posição de cada buraco(em ordem dos objetos):',objetos[3])
input()

