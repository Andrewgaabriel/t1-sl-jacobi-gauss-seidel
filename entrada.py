


# Carrega em uma matriz a placa em L
# Ela vem em um arquivo de texto da forma:
"""
    0   25  30  0   0
    70  x   x   20  0
    80  x   x   x   10
    100 x   x   x   15
    0   90  110 120 0 
"""
# Onde x são os pontos que queremos calcular, 0 são pontos que não existem e os outros são pontos que já temos
# A temperatura em cada ponto é a média aritmética das temperaturas dos pontos vizinhos


def carrega_placa():
    placa = []
    with open('placa.txt', 'r') as f:
        for line in f:
            placa.append([float(x) if x != 'x' else None for x in line.split()])
    return placa

def main():
    placa = carrega_placa()
    print(placa)
    
if __name__ == '__main__':
    main()
    
    