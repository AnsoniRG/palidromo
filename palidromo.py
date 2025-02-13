word = input('palabra: ')

def ispalidodromo(a):
  copia = a
  copia = list(copia)
  copia.reverse()
  if(list(a) == copia):
    print('Es palindromo')

    ispalidodromo(word)

