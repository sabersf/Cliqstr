import numpy as np
import networkx as nx
# calculate the length of a generator
def generator_size(g):
    return sum(1 for x in g)
def cliqstr(g):
    # finding the maximal cliques using bron kerbosch algorithm in networkx 
    cliq = nx.find_cliques(g)
    # converting the generator type to a 2d list
    counter = 0
    cliques = []
    for i in nx.find_cliques(g):
        if len(i)>1:
            cliques.append(i)
            counter += 1
    #assert cliques_size == counter
    print cliques
    cliques_size = counter
    vecd = np.zeros(counter)
    matA = np.zeros((counter, counter))
    cliq_list = [counter]
    # Calculating matX and vector D in the formula
    for i in range(counter):
        for j in range(counter):
            matA[i,j] = len(set(cliques[i]).intersection(cliques[j]))*(len(set(cliques[i]).intersection(cliques[j])) -1)/2
        matA[i,i] = len(cliques[i]) * (len(cliques[i]) - 1) / 2
        for j in cliques[i]:
            for k in cliques[i]:
                if j!=k:
                    if g.has_edge(j,k):
                         vecd[i] += 1
    vecd /= 2
    # Solving the system of equations 
    #eps = 0.0000000001
    #print matA
    print vecd
    Mu = np.linalg.tensorsolve(matA,vecd)
    return Mu
