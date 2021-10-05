import os #Importamos a biblioteca os
import time #Importamos a biblioteca time (para trabalhar com o tempo de execução)

with open('HOSTS.txt') as file: #Com a abertura do HOSTS.txt como arquivo, vamos criar uma variável chamdada dump, e dizer para ela ler o arquivo e jogar dentro da variável dump
    dump = file.read()
    dump = dump.splitlines() #Colocou os ips em linhas separadas

    for ip in dump: #Para cada ip em dump vamos printar a verificação do ip
        print('Verificando o ip: ', ip)
        print('-' * 60)
        os.system('ping -n 2 {} ' .format(ip)) #Envia dois pacotes e formata o ip para dentro da {}
        print('-' * 60)
        time.sleep(5)  #Faz uma espera de 5 segundos no tempo de execução de um comando para o outro