import numpy as np
import networkx as nx
# calculate the length of a generator
def generator_size(g):
    return sum(1 for x in g)
def cliqstr(g):
    # finding the maximal cliques using bron kerbosch algorithm in networkx 
    cliq = nx.find_cliques(g)
    cliques_size = generator_size(nx.find_cliques(g))
    vecd = np.zeros(cliques_size)
    matA = np.zeros((cliques_size, cliques_size))
    cliq_list = [cliques_size]
    # converting the generator type to a 2d list
    counter = 0
    cliques = [[] for i in cliq]
    for i in nx.find_cliques(g):
        cliques[counter] = i
        counter += 1
    assert cliques_size == counter
    # Calculating matX and vector D in the formula
    for i in range(cliques_size):
        for j in range(cliques_size):
            matA[i,j] = len(set(cliques[i]).intersection(cliques[j]))*(len(set(cliques[i]).intersection(cliques[j])) -1)/2
        matA[i,i] = len(cliques[i]) * (len(cliques[i]) - 1) / 2
        for j in cliques[i]:
            for k in cliques[i]:
                if j!=k:
                    if G.has_edge(j,k):
                         vecd[i] += 1
    vecd /= 2
    # Solving the system of equations 
    Mu = np.linalg.solve(matA,vecd)
    return Mu
    
