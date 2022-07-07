pedras, sapos = map(int, input().split())

posi = []
for i in range(pedras):
    posi.append(0)

inicial, pulo, soma = 0, 0, 0

for i in range(sapos):
    inicial, pulo = map(int, input().split())
    soma = inicial
    posi[soma-1] = 1
    while soma <= pedras:
        soma += pulo
        if soma <= pedras:
            posi[soma-1] = 1
        else:
            pass
    while soma >= 1:
        soma -= pulo
        if soma >= 1:
            posi[soma-1] = 1
        else:
            pass

for i in range(pedras):
    print(posi[i])