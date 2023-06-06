import copy
import time


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
def sistemaLinear(placaOriginal):
    
    #copia a placa para não alterar a original
    placa = [x[:] for x in placaOriginal]
    equacoes = []
        
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
                
                
                # Adiciona a divisão por 4
                equacao.append('/4')
                
                equacoes.append(equacao)
                
                # Adiciona a equação na placa
                placa[i][j] = 'T'+str(i)+str(j)
                
    return equacoes

    
    
    
def jacobi(equacoes):
    print('Aplicando Jacobi...')
    
    
    tempoInicial = time.time()
    
    equacoesdict = {}
    for i in range(len(equacoes)):
        equacoesdict[equacoes[i][0]] = equacoes[i][1:]    
    equacoesbasedict = copy.deepcopy(equacoesdict)

    
    
    # Cria uma lista com os valores atuais de cada ponto
    valoresAtuais = {}
    for i in range(len(equacoes)):
        valoresAtuais[equacoes[i][0]] = 0        
        

    # Cria uma lista com os valores anteriores de cada ponto
    valoresAnteriores = {}
    for i in range(len(equacoes)):
        valoresAnteriores[equacoes[i][0]] = 0        
        
        
        
    iteracoes = 0
    
    # Aplica o método de Jacobi
    while True:
        
        iteracoes += 1
        valoresAnteriores = copy.deepcopy(valoresAtuais)
        
        for i in equacoesdict.keys():

            # Substitui as vaiáveis pelos valores atuais
            for j in range(len(equacoesdict[i])):

                
                if equacoesbasedict[i][j] == '/4': # Se for a divisão por 4,
                    continue
                if type(equacoesbasedict[i][j]) is str: # Se for uma variável
                    equacoesdict[i][j] = valoresAtuais[equacoesbasedict[i][j]]
        
        for i in equacoesdict.keys():
            # Calcula o valor do ponto atual
            valoresAtuais[i] = sum(equacoesdict[i][:-1])/4
        

        erro = calcula_erro(valoresAtuais, valoresAnteriores)
        
        if erro < precisao:
            break
        else:
            continue
    
    #Fim contador
    tempoFinal = time.time()
    
    print("     + Resultados Jacobi + \n")
    print(' - Tempo de execução: (ms) ', (tempoFinal - tempoInicial)*1000)
    print(' - Tempo de execução: (s)', tempoFinal - tempoInicial, ' segundos')
    print(' - Tempo de execução: (min)', (tempoFinal - tempoInicial)/60, ' minutos')
    print(' - Iterações: ', iteracoes)
    print(' - Valores finais: ', valoresAtuais)
    
    
    


    
    
    

 
    
def calcula_erro(valoresAtuais : dict, valoresAnteriores : dict):
    valoresAtuais = list(valoresAtuais.values())
    valoresAnteriores = list(valoresAnteriores.values())
    erros = list(map(lambda x, y: x-y, valoresAtuais, valoresAnteriores))
    erro = sum(list(map(lambda x: x**2, erros)))**0.5
    return erro
    


def gauss_seidel(equacoes):
    print('Gauss-Seidel')
    
    tempoInicial = time.time()
    
    equacoesdict = {}
    for i in range(len(equacoes)):
        equacoesdict[equacoes[i][0]] = equacoes[i][1:]
    
    equacoesbasedict = copy.deepcopy(equacoesdict)
    
        
    
    
    # Cria uma lista com os valores atuais de cada ponto
    valoresAtuais = {}
    for i in range(len(equacoes)):
        valoresAtuais[equacoes[i][0]] = 0
        
        
        
    # Cria uma lista com os valores anteriores de cada ponto
    valoresAnteriores = {}
    for i in range(len(equacoes)):
        valoresAnteriores[equacoes[i][0]] = 0
    
    
    
        
        
        
    valoresEncontrados = {}
    for i in range(len(equacoes)):
        valoresEncontrados[equacoes[i][0]] = 0
        
        
    iteracoes = 0
    
    while True:
        
        iteracoes += 1
        valoresAnteriores = copy.deepcopy(valoresEncontrados)
        # limpa a lista de valores encontrados
        for i in valoresEncontrados.keys():
            valoresEncontrados[i] = 0

        
        
        
        for i in equacoesdict.keys():
            equacao = []
        
            # Substitui as vaiáveis pelos valores atuais
            for j in range(len(equacoesdict[i])):

                
                if equacoesbasedict[i][j] == '/4': # Se for a divisão por 4,
                    continue
                
                
                 # Se for uma variável e não estiver na lista de valores encontrados
                if type(equacoesbasedict[i][j]) is str and valoresEncontrados[equacoesbasedict[i][j]] == 0:
                    equacao.append(valoresAnteriores[equacoesbasedict[i][j]])
                
                
                 # Se for uma variável e estiver na lista de valores encontrados
                elif type(equacoesbasedict[i][j]) is str and valoresEncontrados[equacoesbasedict[i][j]] != 0:
                    equacao.append(valoresEncontrados[equacoesbasedict[i][j]])
                    
                elif type(equacoesbasedict[i][j]) is int or type(equacoesbasedict[i][j]) is float:
                    equacao.append(equacoesbasedict[i][j])
                    
            valoresEncontrados[i] = sum(equacao)/4

                    
        
        

        erro = calcula_erro(valoresEncontrados, valoresAnteriores)
        
        if erro < precisao:
            break
        else:
            continue
    
    #Fim contador
    tempoFinal = time.time()
    
    print("     + Resultados Gauss-Seidel + \n")
    print(' - Tempo de execução: (ms) ', (tempoFinal - tempoInicial)*1000)
    print(' - Tempo de execução: (s)', tempoFinal - tempoInicial, ' segundos')
    print(' - Tempo de execução: (min)', (tempoFinal - tempoInicial)/60, ' minutos')
    print(' - Iterações: ', iteracoes)
    print(' - Valores finais: ', valoresEncontrados)
    
    




precisao = 0.000001

def main():
    placa = carrega_placa()
    print(placa)
    
    # precisao = 10**(-6)
    
    # Pede para o usuário definir qual método quer usar, sendo 1 para Jacobi e 2 para Gauss-Seidel
    metodo = int(input('+ Opções:\n 1 - Jacobi\n 2 - Gauss-Seidel\n 3 - Ambos\n\n Escolha uma opção:'))
    
    equacoes = sistemaLinear(placa)
      
        
    # Escrevendo de forma clara as equacoes em um arquivo
    with open('sistema.txt', 'w') as f:
        for i in equacoes:
            f.write(str(i[0]) + ' = ' + '(' + str(i[1]) + ' + ' + str(i[2]) + ' + ' + str(i[3]) + ' + ' + str(i[4]) + ')' + str(i[5]) + '\n')
            
        
    if metodo == 1:
        jacobi(equacoes)
    elif metodo == 2:
        gauss_seidel(equacoes)
    elif metodo == 3:
        jacobi(equacoes)
        gauss_seidel(equacoes)
    else:
        print('Método inválido')
        return
    
    
if __name__ == '__main__':
    main()
    
    