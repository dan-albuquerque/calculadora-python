from classes import Operacoes


##############################################################################################################################################

while True:
  print('1 - soma')
  print('2 - subtração')
  print('3 - multiplicação')
  print('4 - divisão')
  print('5 - potenciação')
  print('6 - raiz quadrada')
  print('7 - sair\n\n')
  
  try:

    operador = int(input('digite a operação que deseja realizar: '))

    #soma

    if operador == 1:
      numeros = input('digite os números que deseja somar: ')
      numeros = Operacoes.converter_inteiros(numeros)
      resposta = Operacoes.soma(numeros)
      print(f'\n{resposta}\n')

    #subtração

    elif operador == 2:
      numeros = input('digite os números que deseja subtrair ')
      numeros = Operacoes.converter_inteiros(numeros)
      resposta = Operacoes.subtracao(numeros)
      print(f'\n{resposta}\n')

    #multiplicação

    elif operador == 3:
      numeros = input('digite os números que deseja multiplicar: ')
      numeros = Operacoes.converter_inteiros(numeros)
      resposta = Operacoes.multiplicacao(numeros)
      print(f'\n{resposta}\n')

    #divisão de apenas 2 números

    elif operador == 4:
      numeros = input('digite dois números que deseja dividir: ')
      numeros = Operacoes.converter_inteiros(numeros)
      if len(numeros) > 2:
        print('digite apenas 2 números!\n')
      else:      
        resposta = Operacoes.divisao(numeros)
        print(f'\n{resposta}\n')

    #potência

    elif operador == 5:
      numero = int(input('digite o número que deseja calcular sua potência: '))
      potencia = int(input('digite a potência que deseja calcular: '))
      resposta = Operacoes.potencia(numero, potencia)
      print(f'\n{resposta}\n')

    #raiz quadrada

    elif operador == 6:
      numero = int(input('digite um número pra calcular sua raiz quadrada: '))
      resposta = Operacoes.raiz_quadrada(numero)
      print(f'\n{resposta}\n')
    
    #terminar o loop
    elif operador == 7:
      break

    else:
      print('digite um valor válido!\n')

  except ValueError:
    print('digite apenas números!\n')
