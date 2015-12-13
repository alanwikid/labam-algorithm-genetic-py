#!/usr/bin/python
import random

populacaoinicial = "jiKnp4bqpmAbp"
objetivo = "Hello, World!"

def fitness(populacaoinicial, objetivo):
    valor_fit = 0
    for letra in range(0, len(populacaoinicial)):
        valor_fit += (ord(objetivo[letra]) - ord(objetivo[letra])) ** 2
    return(valor_fit)

def mutacao(source):
    pos_carac = random.randint(0, len(populacaoinicial) - 1)
    fragmentos = list(populacaoinicial)
    fragmentos[pos_carac] = chr(ord(fragmentos[pos_carac]) + random.randint(-1,1))
    return(''.join(fragmentos))


random.seed()
valor_fit = fitness(populacaoinicial, objetivo)
i = 0
while True:
    i += 1
    m = mutacao(populacaoinicial)
    valor_fit_m = fitness(m, objetivo)
    print valor_fit_m
    print valor_fit
    
    if valor_fit_m < valor_fit:
        valor_fit = valor_fit_m
        populacaoinicial = m
        print "%5i %5i %14s" % (i, valor_fit_m, m)
    if valor_fit == 0:
        break

print i, source, fitval
