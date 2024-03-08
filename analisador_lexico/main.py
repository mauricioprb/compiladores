estados = []
simbolos = []
estadoFinal = []
regrasTransicao = []
estadoAtual = ''


def init():
  global estados, simbolos, estadoFinal, regrasTransicao, estadoAtual
  arquivo = open('./maquina.txt')
  estados = arquivo.readline().strip().split(',')
  simbolos_linha = arquivo.readline().strip()
  estadoFinal = arquivo.readline().strip().split(',')

  for simbolo in simbolos_linha:
    simbolos.append(simbolo)

  linha = arquivo.readline().strip()
  while linha:
    regrasTransicao.append(linha)
    linha = arquivo.readline().strip()

  estadoAtual = estados[0]
  arquivo.close()


def ler_arquivo_input():
  arquivo = open('./input.c')
  linhas = arquivo.readlines()
  for linha in linhas:
    executa_AFD(linha.strip())


def executa_AFD(linha):
  global estadoAtual
  for caracterer in linha:
    for rule in regrasTransicao:
      r = rule.split(':')
      if r[0] == estadoAtual and caracterer in r[1]:
        estadoAtual = r[2]
        #r[0]: estado de origem
        #r[1]: simbolos para ler
        #r[2]: estado de destino
  print(linha, 'está:', estadoAtual)
  reconhecido = 0
  for fs in estadoFinal:
    if fs.split(':')[0] == estadoAtual:
      print('reconhecido como: ', fs.split(':')[1])
      reconhecido = 1
  if not reconhecido:
    print(linha, 'não reconhecido')
  estadoAtual = estados[0]


init()
ler_arquivo_input()
