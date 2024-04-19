from afd import AFD

afd = AFD('./analisador_lexico/maquina.txt', './analisador_lexico')

with open('./analisador_lexico/input.c', 'r') as file:

    index = 1
    for linha in file.readlines():
        linha = linha.strip()
        afd.exec(linha, index)
        index += 1
        print()
