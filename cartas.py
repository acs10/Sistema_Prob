from fractions import Fraction
import random
import itertools

def combos(items , n):
    """Todas as combinações de n items; cada combinação concatenada em uma
    string"""
    return {' '.join(combo) for combo in itertools.combinations(items , n)}

def P(evento , espaco):
    "A probabilidade de um `evento `, dado o `espaco ` amostral"
    return Fraction(len(evento & espaco), len(espaco))


def cross(A, B):
    """O conjunto de formas de concatenar os itens de A e B (produto
    cartesiano)"""
    return {a + b for a in A for b in B}

def P(evento , espaco):
    """A probabilidade de um evento , dado um espaco amostral.
    evento pode ser um conjunto ou um predicado"""
    if callable(evento):
        evento = tal_que(evento, espaco)
    return Fraction(len(evento & espaco), len(espaco))

def tal_que(predicado , colecao):
    """O subconjunto de elementos da colecao para os quais o predicado é
        verdadeiro"""
    return {e for e in colecao if predicado(e)}


def flush(jogada):
    return any(jogada.count(n) == 5 for n in naipes)

naipes = 'SHDC'
graus = 'A23456789TJQK'
baralho = cross(graus , naipes)


jogadas = combos(baralho , 5)

random.sample(jogadas , 5)



prob_flush = P(flush , jogadas)
print('prob_flush')
print(prob_flush)

