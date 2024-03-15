estados = []
simbolos = []
estadoFinal = []
regrasTransicao = []
estadoAtual = ''


def init():
  global estados, simbolos, estadoFinal, regrasTransicao, estadoAtual
  arquivo = open('analisador_lexico/maquina.txt')
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
  arquivo = open('analisador_lexico/input.c')
  linhas = arquivo.readlines()
  for linha in linhas:
    executa_AFD(linha.strip())
  arquivo.close()


def executa_AFD(linha):
  global estadoAtual
  componente = ''
  separadores = {' ', '=', ';'}

  for caracter in linha:
    if caracter in separadores:
      if componente:
        for final in estadoFinal:
          estado, tipo = final.split(':')
          if estadoAtual == estado:
            print(componente.strip() + ": " + tipo)
        componente = ''
      if caracter == '=':
        print(caracter + ": atribuição")
      elif caracter == ';':
        print(caracter + ": ponto e vírgula")
      estadoAtual = 'q0'
    else:
      for rule in regrasTransicao:
        r = rule.split(':')
        if r[0] == estadoAtual and caracter in r[1]:
          estadoAtual = r[2]
          componente += caracter
          break


init()
ler_arquivo_input()
