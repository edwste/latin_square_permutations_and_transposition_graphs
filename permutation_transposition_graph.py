import itertools as it
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import math as mp
import sys
import collections as cl

n=6


sys.setrecursionlimit(3000)

def transpose(element,i,j):
    l=list(element)
    l[i-1],l[j-1]=l[j-1],l[i-1]
    return l

def generate_n_permutation_elements(n):
    l=[i for i in range(1,n+1)]
    import itertools as it
    return it.permutations(l)

def get_non_intersecting_permutations(i,n):
    permutations = [i for i in generate_n_permutation_elements(n)]
    permutation_intersections = []
    for j in permutations:
        if i==j:
            next
        flag=False
        for c,a in enumerate(j):
            if a==i[c]:
                flag=True
                break
        if not flag:
            permutation_intersections.append(j)
    return permutation_intersections


def generate_transposition_set(n):
	return [i for i in it.combinations([i for i in range(1,n+1)],	2)]


def check_permutation_intersection(i,j):
	for c,a in enumerate(i):
		if a==j[c]:
			return False

pe=get_non_intersecting_permutations(tuple([i for i in range(1,n+1)]),n)
print(pe)
transposition_set = generate_transposition_set(n)
edge_list = []


def dfs_permutation(i,trans_set):
	#we want list of edges here
	for a in trans_set:
		#transpose
		trans=transpose(pe[i],a[0],a[1])
		if tuple(trans) not in pe:
			next
		for c,perm in enumerate(pe):
			if trans==list(perm):
				if (pe[i],pe[c]) not in edge_list:
					edge_list.append((pe[i],pe[c]))
					dfs_permutation(c,trans_set)

output=dfs_permutation(0,transposition_set)

G=nx.Graph()
G.add_nodes_from(pe)
G.add_edges_from(edge_list)

#get edge count of each node
edge_count_list=[]
for i,p in enumerate(pe):
	edge_count = 0
	for edge in edge_list:
		if edge[0]==p:
			edge_count = edge_count + 1
	edge_count_list.append(edge_count)
print(edge_count_list)
c=cl.Counter(edge_count_list)
print(c)

#color nodes
node_colors = []
colors = ['red','yellow','blue','green','orange','red','yellow','blue','green','orange','yellow','blue','red']
for i in edge_count_list:
	node_colors.append(colors[i])

#partite check
counter=0
for e in edge_list: 
	i1,i2 = pe.index(e[0]),pe.index(e[1])
	if edge_count_list[i1]==edge_count_list[i2]:
		print(pe[i1],pe[i2],edge_count_list[i1],edge_count_list[i2])
		counter=counter+1
print(counter)

nx.draw(G, with_labels=True,node_color=node_colors)
plt.show()