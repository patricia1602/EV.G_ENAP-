#Exercício: escreva uma função para testar se uma palavra do usuário é um palíndromo.

def verifica_palindromo(palavra):
    palavra = palavra.lower()
    return palavra == palavra[::-1]

palavra_usuario  = input("Digite um palavra para verificar se é um palíndromo: ")
if verifica_palindromo(palavra_usuario):
   print( f"A palavra '{palavra_usuario}' é um palíndromo!")
else:
   print(f"A palavra '{palavra_usuario}' não é palíndromo.")