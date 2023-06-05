


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




# Cria uma lista de equações para cada ponto que queremos calcular (i.e um sistema linear)
def sistemaLinear(placa):
    
    # Percorre cada linha da placa extraindo as equações de cada ponto
    for i in range(len(placa)):
        for j in range(len(placa[i])):
            # Se o ponto for None, então ele é um ponto que queremos calcular
            # Então, criamos uma equação para ele e adicionamos a lista de equações
            if placa[i][j] is None:
                equacao = []
                
                # O ponto atual é o ponto que queremos calcular
                # equacao.append('x')
                equacao.append('T'+str(i)+str(j))                
                
                
                # Os outros pontos são os pontos vizinhos e serão identificados por Tij
                # Se o ponto vizinho for None, então ele é um ponto que queremos calcular
                # Então, adicionamos ele a equação
                # Se não, adicionamos o valor dele na equação
                if i > 0:
                    if placa[i-1][j] is None:
                        # equacao.append('x')
                        equacao.append('T'+str(i-1)+str(j))
                    else:
                        equacao.append(placa[i-1][j])
                if i < len(placa)-1:
                    if placa[i+1][j] is None:
                        #equacao.append('x')
                        equacao.append('T'+str(i+1)+str(j))
                    else:
                        equacao.append(placa[i+1][j])
                if j > 0:
                    if placa[i][j-1] is None:
                        #equacao.append('x')
                        equacao.append('T'+str(i)+str(j-1))
                        
                    else:
                        equacao.append(placa[i][j-1])
                if j < len(placa[i])-1:
                    if placa[i][j+1] is None:
                        #equacao.append('x')
                        equacao.append('T'+str(i)+str(j+1))
                    else:
                        equacao.append(placa[i][j+1])
                
                # Adiciona a equação na placa
                placa[i][j] = equacao
    # Cria uma lista com todas as equações (i.e sistema linear)
    sistema = []
    for i in range(len(placa)):
        for j in range(len(placa[i])):
            if type(placa[i][j]) is list:
                sistema.append(placa[i][j])
    return sistema

    
    
    
def jacobi(sistemaLinear):
    print('Jacobi')
 
    
    
def gauss_seidel(sistemaLinear):
    print('Gauss-Seidel')



precisao = 0.000001

def main():
    placa = carrega_placa()
    print(placa)
    
    # precisao = 10**(-6)
    
    # Pede para o usuário definir qual método quer usar, sendo 1 para Jacobi e 2 para Gauss-Seidel
    metodo = int(input('Digite 1 para Jacobi ou 2 para Gauss-Seidel: '))
    
    sistemalinear = sistemaLinear(placa)
    
    
    if metodo == 1:
        jacobi(sistemalinear)
    elif metodo == 2:
        gauss_seidel(sistemalinear)
    else:
        print('Método inválido')
        return
    
    
if __name__ == '__main__':
    main()
    
    