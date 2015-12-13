# -*- coding: utf-8 -*-
import random

#Comprimento do Cromossomo
COMP = 36 
#Valores que o gene pode ter
#alelos = (0,1)
#População
TAM = 1500
fit = []
pop = []
pop_temp = []


pc = 0.6 # probabilidade de crossover
pm = 0.03 # probabilidade de mutação

def gerar():
    """GERANDO POPULAÇÂO INICIAL"""
    for i in range(TAM):
        #Cria uma nova linha na matriz
        pop.append([])
        
        for j in range(COMP):
            valor = (random.randint(0,100))
            #Resolve valor de cada alelo
            if (valor < 50):
                pop[i].append(0)
            else:
                pop[i].append(1)
    for i in range(TAM):
        print  i+1,":" ,pop[i], len(pop[i])
    #biologia digital

def fitness():
    """CALCULANDO FITNESS"""
    
    for i in range(TAM):
        if len(fit) < TAM:
            fit.append([])
        

        tmp = 0
        
        tmp += 9 + pop[i][2] * pop[i][5] - pop[i][23] * pop[i][14] + pop[i][24] * pop[i][4] - pop[i][21] * pop[i][10]
        + pop[i][36] * pop[i][15] - pop[i][11] * pop[i][26] + pop[i][16] * pop[i][17] + pop[i][3] * pop[i][33]
        + pop[i][28] * pop[i][19] + pop[i][12] * pop[i][34] - pop[i][31] * pop[i][32] - pop[i][22] * pop[i][25]
        + pop[i][35] * pop[i][27] - pop[i][29] * pop[i][7] + pop[i][8] * pop[i][13] - pop[i][6] * pop[i][9]
        + pop[i][18] * pop[i][20] - pop[i][1] * pop[i][30] + pop[i][23] * pop[i][4] + pop[i][21] * pop[i][15]
        + pop[i][26] * pop[i][16] + pop[i][31] * pop[i][12] + pop[i][25] * pop[i][19] + pop[i][7] * pop[i][8]
        + pop[i][9] * pop[i][18] + pop[i][1] * pop[i][33]

        """
        tmp += 9 + pop[i][2-1] * pop[i][5-1] - pop[i][23-1] * pop[i][14-1] + pop[i][24-1] * pop[i][4-1] - pop[i][21-1] * pop[i][10-1]
        + pop[i][36-1] * pop[i][15-1] - pop[i][11-1] * pop[i][26-1] + pop[i][16-1] * pop[i][17-1] + pop[i][3-1] * pop[i][33-1]
        + pop[i][28-1] * pop[i][19-1] + pop[i][12-1] * pop[i][34-1] - pop[i][31-1] * pop[i][32-1] - pop[i][22-1] * pop[i][25-1]
        + pop[i][35-1] * pop[i][27-1] - pop[i][29-1] * pop[i][7-1] + pop[i][8-1] * pop[i][13-1] - pop[i][6-1] * pop[i][9-1]
        + pop[i][18-1] * pop[i][20-1] - pop[i][1-1] * pop[i][30-1] + pop[i][23-1] * pop[i][4-1] + pop[i][21-1] * pop[i][15-1]
        + pop[i][26-1] * pop[i][16-1] + pop[i][31-1] * pop[i][12-1] + pop[i][25-1] * pop[i][19-1] + pop[i][7-1] * pop[i][8-1]
        + pop[i][9-1] * pop[i][18-1] + pop[i][1-1] * pop[i][33-1]
            

        """
            
        
        #print "valor de i é:", i
        #print "tamanho", len(fit)
        fit[i] = tmp
        
    for i in range(TAM):
        print i+1, ":", fit[i]


def torneio():
    """SELEÇÂO  POR TORNEIO"""
    nro = 3
    for i in range(TAM):
        pop_temp.append([])
        indice = 0
        for j in range(nro):
            indice = random.randint(0, TAM-1)
            if (j == 0):
                indmaior = indice
            else:
                if (fit[indice] > fit[indmaior]):
                    indmaior = indice
        for k in range(COMP):
            pop_temp[i].append(pop[indmaior][k])
    for i in range(TAM):
        print i+1, "Temporario:", pop_temp[i]


def crossover():
    #global prob
    
    for i in range(0,TAM,2):
        pai = pop_temp[i]
        mae = pop_temp[i+1]
        random.seed()
        prob = random.random()
        
        if prob<=pc:
            print "CROSSOVER:=================="
            corte = random.randint(0, len(pop_temp[i]) - 1)
            
            #fim = random.randint(1, len(pop_temp[i]) -2)
            filho1 = pai[:corte] + mae[corte:]
            filho2 = mae[:corte] + pai[corte:] 
            pop[i] = filho1
            pop[i+1] = filho2
            print i+1,  "Pai:     ", pai
            print i+2,  "Mãe:     ", mae
            print i+1,  "Filho1:  ", pop[i]
            print i+2,"Filho2:  ", pop[i+1]
            print "============================"
        else:
            pop[i] = pai
            pop[i+1] = mae
            print i+1, ":", pop[i]
            print i+2, ":", pop[i+1]
    #for i in range(TAM):
    #    print i , ":", pop[i]



def mutacao():
    #filho_dna = pop['dna'][:]
    for i in range(TAM):
        if random.random() <= pm:
            print "MUTACAÇÂO:=================="
            print i+1, "Anterior:", pop[i]
            posicao = random.randint(0, COMP-1)
         #   pop[i] = random.randint(0, 1)
            if (pop[i][posicao] == 0):
                pop[i][posicao] = 1
            else:
                pop[i][posicao] = 0
            
            print i+1, "Atual   :", pop[i]
            print "============================"
        else:
            print i+1, ":", pop[i]
                
    


gerar()
fitness()
torneio()
crossover()
fitness()
mutacao()
fitness()

