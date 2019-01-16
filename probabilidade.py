from fractions import Fraction
#PROBABILIDADE
def P(evento , espaco):
    "A probabilidade de um `evento `, dado o `espaco ` amostral"
    return Fraction(len(evento & espaco), len(espaco))

A = {1,2,3,4,5,6}
E1 = {1}
E2 = {1,7,8}
E3 = {1,2,3}
E4 = {6,5,3,2,1}

print(P(E1,A))
print(P(E2,A))
print(P(E3,A))
print(P(E4,A))

print('')
#o conjunto dos resultados que atendem ao predicado “dado com face par”.

par = {2, 4, 6}
print(P(par , A))
print('')
'''O tipo Fraction do Python é usado para representar valores na forma de frações (racional). Por
exemplo:'''
print(Fraction (0.5))
print(Fraction (0.3))

# usa limit_denominator () para encontrar a fração mais aproximada
print(Fraction (0.3).limit_denominator ())

print(Fraction (3, 10))
print(Fraction (0.3333333))

# limitando o denominador (padrão é max =1000000)
print(Fraction (0.3333333).limit_denominator ())

'''conjunto de todas as combinações com 6
bolas. O código a seguir define a função combos():'''

#O código a seguir define a função cross() e o conteúdo da urna:
import itertools
import random

def cross(A, B):
    "O conjunto de formas de concatenar os itens de A e B (produtocartesiano)"
    return {a + b
            for a in A for b in B
            }

def combos(items , n):
    "Todas as combinações de n items; cada combinação concatenada em uma string"
    return {' '.join(combo)
            for combo in itertools.combinations(items , n)
            }

urna = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')
                                                               
U6=combos(urna , 6)
print(random.sample(U6 , 10))
#quantidade de U6
print(len(U6))

#a função escolha():

from math import factorial

def escolha(n, c):
    "Número de formas de escolher c itens de uma lista com n items"
    return factorial(n) // (factorial(c) * factorial(n - c))

print(escolha(23, 6))

#Problema 1: qual a probabilidade de selecionar 6 bolas vermelhas?
red6 = {s for s in U6 if s.count('R') == 6}
prob_red6 = P(red6 , U6)
print('A probabilidade de selecionar 6 bolas vermelhas é',prob_red6)
print(float(prob_red6),'%')
#Por que 84 escolhas possíveis? Por que há 9 bolas vermelhas na urna, então estamos querendo
#saber quantas são as formas de escolher 6 delas:
print(escolha (9, 6))

print('A probabilidade de selecionar 6 bolas vermelhas é',prob_red6)
#O código verifica se o valor de P(red6, U6) é igual a Fraction(escolha(9, 6), len(U6)). O resultado é: True.
print(P(red6 , U6) == Fraction(escolha (9, 6), len(U6)))

#Problema 2: qual a probabilidade de escolher 3 azuis, 2 brancas e 1 vermelha?
red6 = {s for s in U6 if s.count('B') == 3 and s.count('W') == 2 and s.count('R') == 1}
prob_red6 = P(red6 , U6)
print('A probabilidade de escolher 3 azuis, 2 brancas e 1 vermelha é',prob_red6)
print(float(prob_red6),'%')

#Problema 3: Qual a probabilidade de termos exatamente 4 bolas brancas?
w4 = {s for s in U6 if s.count('W') == 4}
prob_w4 = P(w4 , U6)
print('A probabilidade de termos exatamente 4 bolas brancas é',prob_w4)
print(float(prob_w4),'%')
