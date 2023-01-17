class Operacoes:

  #processo de receber uma serie de numeros e transforma-los em uma lista de números

  def converter_inteiros(numeros):
    lista_numeros = numeros.split()
    
    for i in range(len(lista_numeros)):

      lista_numeros[i] = float(lista_numeros[i])
      
    return lista_numeros

  #operações 

  def soma(lista_numeros):
    resultado = 0

    for i in lista_numeros:

      resultado += i
      
    return resultado

  def subtracao(lista_numeros):

    resultado = lista_numeros[0]

    for i in range(1,len(lista_numeros)):

      resultado -= lista_numeros[i]

    return resultado

  def multiplicacao(lista_numeros):
    resultado = 1

    for i in lista_numeros:

      resultado *= i

    return resultado

  def divisao(lista_numeros):

    try:
      ans = f'{lista_numeros[0] / lista_numeros[1]:.2f}' 
      return ans
    except ZeroDivisionError:
      return 'não é possível fazer uma divisão com zero\n'

  def potencia(numero, potencia):

    return numero ** potencia

  def raiz_quadrada(n1):

    return n1 ** 1/2
