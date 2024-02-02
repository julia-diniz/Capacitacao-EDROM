##Júlia Diniz##
##Trabalho 1 - Behaviour##
    
def posicao_ponto():
    x = float(input("Digite a coordenada x: "))
    y = float(input("Digite a coordenada y: "))
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))

    centro_x = largura / 2
    centro_y = altura / 2

    if x > largura or y > altura:
        print("As coordenadas do ponto não são válidas para o retângulo informado.")
    else:
        if x == centro_x and y == centro_y:
            print("O ponto informado encontra-se centralizado no retângulo.")
        else:
            if x < centro_x:
                posicao_x = "esquerda"
            elif x > centro_x:
                posicao_x = "direita"
            else:
                posicao_x = "mediana"

            if y < centro_y:
                posicao_y = "inferior"
            elif y > centro_y:
                posicao_y = "superior"
            else:
                posicao_y = "mediana"

            print(f"O ponto encontra-se na porção {posicao_y} em relação ao eixo x e na parte {posicao_x} em relação ao eixo y.")

posicao_ponto()
