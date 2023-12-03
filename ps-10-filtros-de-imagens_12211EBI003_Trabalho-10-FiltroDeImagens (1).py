##Júlia Cristina Rodrigues Diniz##
##12211EBI003##
##Trabalho 10 - Filtro de Imagens##

def main(): #Definindo a função principal (main)
    tipoFiltro = input() #Definindo qual tipo de filtro será utilizado na imagem
    formatoArquivo = input() #Recebendo o valor P2 que indica o formato do arquivo
    colunasLinhas = [i for i in input().split()] #Recebendo valores para definir a quantidade de pixels que formarão as linhas e colunas do arquivo
    maximoPixel = int(input()) #Recebendo o número 255 que indica o valor máximo que um pixel pode conter

    linhasPixels = [] #Criando uma lista para receber as linhas de pixels da imagem

    pixels = [] #Criando uma lista para receber todos os valores de pixels alinhados

    for j in range(int(colunasLinhas[1])): #Repetindo o input até que sejam preenchidas todas as colunas conforme o valor dado em colunasLinhas
        linha = [k for k in input().split()] #Definindo valores que serão adicionados na lista de pixels
        linhasPixels.append(linha) #Adicionando cada valor de pixel contido na imagem em uma lista

    pixels = separaPixelsLinha(linhasPixels, pixels) #Chamando a função que irá preencher a lista pixels

    if (tipoFiltro == "negativo"): #Se o filtro escolhido for do tipo negativo
        calculaNegativo(maximoPixel, pixels) #Chamando função que irá calcular os novos valores para os pixels 

    if (tipoFiltro == "mediana"): #Se o filtro escolhido for do tipo mediana
        listaPixelsOriginal = pixels[:] #Duplicando a lista para guardar os valores da imagem original
        calculaMediana(listaPixelsOriginal, colunasLinhas, pixels) #Chamando função que irá calcular os novos valores para os pixels

    if (tipoFiltro == "edge-detect"): #Se o filtro escolhido for do tipo edge detect
        a = -1
        b = -1
        c = -1
        d = -1
        e = 8  #Definindo valores para cada filtro que possui uma matriz núcleo M específica
        f = -1
        g = -1
        h = -1
        i = -1
        divisor = 1 #Definindo um valor de D específico para o filtro

        listaPixelsOriginal = pixels[:] #Duplicando a lista para guardar os valores da imagem original
        pixels.clear() #Limpando a lista de pixels atual
        pixels = calculaConvolucao(a, b, c, d, e, f, g, h, i, divisor, listaPixelsOriginal, pixels, colunasLinhas, linhasPixels) #Preenchendo a lista com os novos valores

    if (tipoFiltro == "sharpen"): #Se o filtro escolhido for do tipo sharpen
        a = 0
        b = -1
        c = 0
        d = -1
        e = 5  #Definindo valores para cada filtro que possui uma matriz núcleo M específica
        f = -1
        g = 0
        h = -1
        i = 0
        divisor = 1 #Definindo um valor de D específico para o filtro

        listaPixelsOriginal = pixels[:] #Duplicando a lista para guardar os valores da imagem original
        pixels.clear() #Limpando a lista atual de pixels
        pixels = calculaConvolucao(a, b, c, d, e, f, g, h, i, divisor, listaPixelsOriginal, pixels, colunasLinhas, linhasPixels) #Preenchendo a lista com os novos valores

    if (tipoFiltro == "blur"): #Se o filtro escolhido for do tipo blur
        a = 1
        b = 1
        c = 1
        d = 1
        e = 1  #Definindo valores para cada filtro que possui uma matriz núcleo M específica
        f = 1
        g = 1
        h = 1
        i = 1
        divisor = 9 #Definindo um valor de D específico para o filtro

        listaPixelsOriginal = pixels[:] #Duplicando a lista para guardar os valores da imagem original
        pixels.clear() #Limpando a lista atual de pixels
        pixels = calculaConvolucao(a, b, c, d, e, f, g, h, i, divisor, listaPixelsOriginal, pixels, colunasLinhas, linhasPixels) #Preenchendo a lista com os novos valores

    numeroLinhas = int(colunasLinhas[1]) #Buscando valor que define a quantidade de linhas que representam a imagem
    numeroColunas = int(colunasLinhas[0]) #Buscando valor que define a quantidade de colunas que representam a imagem

    if (tipoFiltro == "edge-detect" or tipoFiltro == "sharpen" or tipoFiltro == "blur"): #Se o filtro escolhido utilizar uma operação de convolução
        #Os pixels da borda não são incluídos na imagem resultante
        numeroLinhas = numeroLinhas - 2 #Removendo as duas linhas da borda do total
        numeroColunas = numeroColunas - 2 #Removendo as duas colunas da borda do total

    print(formatoArquivo) #Imprimindo o formato escolhido para o arquivo(P2)
    print(numeroColunas, numeroLinhas) #Imprimindo os valores que definem a quantidade de linhas e colunas que contém os pixels da imagem
    print(maximoPixel) #Imprimindo o valor máximo que um pixel pode assumir, que nesse caso é 255

    for n in range(numeroLinhas): #Executando programa até que todas as linhas tenham sido percorridas
        n = n + 1 #Calculando n para cada linha da matriz
        rangeFor = numeroColunas * n #Calculando a quantidade de elementos que farão parte de cada linha
        for o in range(rangeFor - numeroColunas, rangeFor): #Verificando cada elemento que pertence à linha
            if (int(pixels[o]) < 0): #Caso um pixel tenha valor negativo
                pixels[o] = 0 #Esse deve ser substituído por 0
            if (int(pixels[o]) > maximoPixel): #Caso um pixel tenha valor maior do que o máximo
                pixels[o] = maximoPixel #Esse deve ser substituído por 255
            if (rangeFor - o != 1): #Caso a subtração do número de elementos pelo número de posições seja difente de 1(por exemplo, uma lista de 24 elementos cujas posições da lista vão de 0-23
                print(pixels[o], end=" ") #Adiciona espaço entre elementos da lista
            else: #Caso seja igual a 1
                print(pixels[o], end="\n") #Cria uma nova linha


def calculaNegativo(maximoPixel, pixels): #Definindo função que calcula valores para filtro negativo
    for m in range(len(pixels)): #Percorrendo os valores de pixels contidos na lista que representa a imagem
        if (int(pixels[m]) == 0): #Caso o valor que descreve a intensidade seja 0(preto)
            pixels[m] = maximoPixel #Esse é substituído pelo valor máximo 255(branco)
        else: #Para o restante dos casos
            pixels[m] = maximoPixel - int(pixels[m]) #O valor dos pixels é calculado subtraindo do valor máximo que ele pode assumir(255)
    
    return pixels #Retornando a lista que contém os novos valores após aplicar o filtro


def calculaMediana(listaPixelsOriginal, colunasLinhas, pixels,): #Definindo função que calcula valores para filtro mediana
    for p in range(len(pixels)): #Percorrendo os valores de pixels contidos na lista que representa a imagem
        listaMascara = [] #Criando uma lista para a máscara(valor da mediana da matriz que circunda o pixel)
        #Como todos os valores dos pixels agora se encontram numa mesma linha, utiliza-se a quantidade de colunas para que seja possível encontrar o valor do elemento contido na posição
        if ((p - int(colunasLinhas[0]) - 1) >= 0 and p % int(colunasLinhas[0]) != 0): #Verificando se existe um valor na posição p(x-1, y-1)
            listaMascara.append(listaPixelsOriginal[p - int(colunasLinhas[0]) - 1]) #Caso exista, esse valor é adicionado à lista que contém os pixels da máscara
        if ((p - int(colunasLinhas[0])) >= 0): #Verificando se existe um valor na posição p(x-1, y)
            listaMascara.append(listaPixelsOriginal[p - int(colunasLinhas[0])]) #Caso exista, esse valor é adicionado à lista que contém os pixels da máscara
        if ((p - int(colunasLinhas[0]) + 1) >= 0 and (p + 1) % int(colunasLinhas[0]) != 0): #Verificando se existe um valor na posição p(x-1, y+1)
            listaMascara.append(listaPixelsOriginal[p - int(colunasLinhas[0]) + 1]) #Caso exista, esse valor é adicionado à lista que contém os pixels da máscara
        if ((p - 1) >= 0 and p % int(colunasLinhas[0]) != 0): #Verificando se existe um valor na posição p(x, y-1)
            listaMascara.append(listaPixelsOriginal[p - 1]) #Caso exista, esse valor é adicionado à lista que contém os pixels da máscara
        listaMascara.append(listaPixelsOriginal[p]) #Adicionando à lista da máscara o valor central que se procura substituir
        if ((p + 1) <= len(pixels) - 1 and (p + 1) % int(colunasLinhas[0]) != 0): #Verificando se existe um valor na posição p(x, y+1)
            listaMascara.append(listaPixelsOriginal[p + 1]) #Caso exista, esse valor é adicionado à lista que contém os pixels da máscara
        if ((p + int(colunasLinhas[0]) - 1) <= len(pixels) - 1 and p != 0 and p % int(colunasLinhas[0]) != 0): #Verificando se existe um valor na posição p(x+1, y-1)
            listaMascara.append(listaPixelsOriginal[p + int(colunasLinhas[0]) - 1]) #Caso exista, esse valor é adicionado à lista que contém os pixels da máscara
        if ((p + int(colunasLinhas[0])) <= len(pixels) - 1): #Verificando se existe um valor na posição p(x+1, y)
            listaMascara.append(listaPixelsOriginal[p + int(colunasLinhas[0])]) #Caso exista, esse valor é adicionado à lista que contém os pixels da máscara
        if ((p + int(colunasLinhas[0]) + 1) <= len(pixels) - 1 and (p + 1) % int(colunasLinhas[0]) != 0): #Verificando se existe um valor na posição p(x+1, y+1)
            listaMascara.append(listaPixelsOriginal[p + int(colunasLinhas[0]) + 1]) #Caso exista, esse valor é adicionado à lista que contém os pixels da máscara

        for q in range(len(listaMascara)): #Para os valores de pixels contidos na lista
            listaMascara[q] = int(listaMascara[q]) #Certificando que sejam tratados como números inteiros e não como strings

        listaMascara.sort() #Ordenando os valores encontrados para que a mediana seja encontrada

        if (len(listaMascara) % 2 != 0): #Se a quantidade de elementos da lista for ímpar 
            posicaoDoMeio = int((len(listaMascara) // 2) + 1) #Encontrando a posição central da lista 
            pixels[p] = listaMascara[posicaoDoMeio - 1] #A mediana da lista é o valor central
        else: #Se a quantidade de elementos contidos na lista for par
            posicaoDoMeioPosterior = int(len(listaMascara) / 2) #Encontrado segundo valor para calcular a mediana
            mediana = int((listaMascara[posicaoDoMeioPosterior - 1] + listaMascara[posicaoDoMeioPosterior])) #Somando o valor das duas posições centrais da lista
            pixels[p] = int(mediana / 2) #A mediana é calculada a partir da média dos dois valores centrais

    return pixels #Retornando a lista que contém os novos valores após aplicar o filtro


def calculaConvolucao(a, b, c, d, e, f, g, h, i, divisor, listaPixelsOriginal, pixels, colunasLinhas, linhasPixels): #Definindo função que calcula valores para filtros que usam convolução
    for u in range(len(listaPixelsOriginal)): #Para os valores de pixels contidos na lista
        listaPixelsOriginal[u] = int(listaPixelsOriginal[u]) #Certificando que sejam tratados como números inteiros e não como strings

    for r in range(len(linhasPixels)): #Percorrendo todas as linhas da lista que representa a imagem 
        if (r > 0): #Se r < 0, a primeira linha da lista é cortada
            if (r != len(linhasPixels) - 1): #Se r = len(linhasPixels) - 1, a última linha da lista é cortada 
                for s in range(len(linhasPixels[r])): #Percorrendo todas as colunas da lista que representa a imagem 
                    if (s > 0): #Se s < 0, a primeira coluna da lista é cortada
                        if (s != len(linhasPixels[r]) - 1): #Se s = len(linhasPixels[r]) - 1, a últim coluna da lista é cortada 
                            pixels.append(int(linhasPixels[r][s])) #Adicionando à pixels a nova lista que exclui os valores contidos na borda

    modificadorPosicao = 0 #Iniciando a contagem da variável que irá modificar as posições em 0 e adicionando 2 a cada linha saltada, já que a primeira e última colunas foram excluídas

    for t in range(len(pixels)): #Percorrendo as posições dos valores de pixels contidos na lista que representa a imagem
        pixelAtual = int(colunasLinhas[0]) + 1 #Encontrando o valor do pixel atual através de uma variável que busca o valor respectivo na lista original 
        if ((t % (int(colunasLinhas[0]) - 2)) == 0 and t != 0): #Se a posição estiver na primeira ou última coluna da linha
            modificadorPosicao = modificadorPosicao + 2 #A cada mudança de linha, é necessário somar duas posições, uma vez que a primeira e a última coluna foram cortadas 

        if (t < int(colunasLinhas[0]) - 2): #Enquanto os pixels estiverem na primeira linha 
            pixelAtual = pixelAtual + t #Somente será adicionado a posição no pixel atual
        else: #Para os valores de pixel que se encontram nas linhas inferiores
            pixelAtual = pixelAtual + t + modificadorPosicao #Além da posição de t, também será adicionado a variável que indica quantas colunas finais e iniciais foram puladas
            
        #Calculando p'(x, y) de acordo com a fórmula fornecida e acessando os valores a partir da lista original
        #Como todos os valores se encontram em uma mesma linha, o número de colunas é utilizado para encontrar a posição correspondente à procurada na matriz
        l1 = a * listaPixelsOriginal[pixelAtual - int(colunasLinhas[0]) - 1] + b * listaPixelsOriginal[pixelAtual - int(colunasLinhas[0])] + c * listaPixelsOriginal[pixelAtual - int(colunasLinhas[0]) + 1]
        #l1 = a * p(x - 1, y - 1) + b * p(x - 1, y) + c * p(x - 1, y + 1)
        l2 = d * listaPixelsOriginal[pixelAtual - 1] + e * \
            listaPixelsOriginal[pixelAtual] + f * \
            listaPixelsOriginal[pixelAtual + 1]
        #l2 = d * p(x, y - 1) + e * p(x, y) + f * p(x, y + 1)
        l3 = g * listaPixelsOriginal[pixelAtual + int(colunasLinhas[0]) - 1] + h * listaPixelsOriginal[pixelAtual + int(colunasLinhas[0])] + i * listaPixelsOriginal[pixelAtual + int(colunasLinhas[0]) + 1]
        #l3 = g * p(x + 1, y - 1) + h * p(x + 1, y) + i * p(x + 1, y + 1)
        pixels[t] = int(l1 + l2 + l3) #Realizando a soma dos valores calculados na fórmula
        pixels[t] = int(pixels[t] / divisor) #Realizando a divisão inteira pelo divisor fornecido

    return pixels #Retornando a lista que contém os novos valores após aplicar o filtro


def separaPixelsLinha(linhasPixels, pixels): #Definindo função que separa todos os pixels e salva na mesma linha de uma lista
    for l in range(len(linhasPixels)): #Percorrendo todos os itens contidos na lista inicial
        for pixel in linhasPixels[l]: #Para cada valor contido na lista de linhasPixels 
            pixels.append(pixel) #Salvando os pixels separados na lista pixel
    
    return pixels #Retornando a lista que contém todos os valores alinhados


main() #Chamando a função principal(main)
##Fim
