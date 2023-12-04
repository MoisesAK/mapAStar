deslocamento = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def calc_manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(mapa, inicio, fim):
    linhas = len(mapa)
    colunas = len(mapa[0])

    custo_atual = {}
    caminho = {}

    custo_atual[inicio] = 0
    fila = [(0, inicio)]

    while fila:
        fila.sort()
        _, posicao_atual = fila.pop(0)

        if posicao_atual == fim:
            break

        for dx, dy in deslocamento:
            proximo_x, proximo_y = posicao_atual[0] + dx, posicao_atual[1] + dy

            if 0 <= proximo_x < linhas and 0 <= proximo_y < colunas and mapa[proximo_x][proximo_y] >= 0:
                custo_suporte = custo_atual[posicao_atual] + mapa[proximo_x][proximo_y]
                vizinho = (proximo_x, proximo_y)

                if vizinho not in custo_atual or custo_suporte < custo_atual[vizinho]:
                    custo_atual[vizinho] = custo_suporte
                    prioridade = custo_suporte + calc_manhattan(fim, vizinho)
                    fila.append((prioridade, vizinho))
                    caminho[vizinho] = posicao_atual

    caminho_completo = []
    posicao_atual = fim
    while posicao_atual != inicio:
        caminho_completo.append(posicao_atual)
        posicao_atual = caminho[posicao_atual]
    caminho_completo.append(inicio)
    caminho_completo.reverse()

    return caminho_completo, custo_atual[fim]

if __name__ == "__main__":
    with open('map.txt', 'r') as file:
        linhas = file.readlines()
        largura, altura = map(int, linhas[0].split())
        x_inicio, y_inicio = map(int, linhas[1].split())

        mapa = []
        for linha in linhas[2:]:
            mapa.append(list(map(int, linha.split())))

    x_fim = int(input("coordenada x do fim "))
    y_fim = int(input("coordenada y do fim "))

    inicio = (x_inicio, y_inicio)
    fim = (x_fim, y_fim)

    caminho, custo = astar(mapa, inicio, fim)

    print(f"{custo} ", end=' ')
    print(*caminho)
