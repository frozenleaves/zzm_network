# -*- coding: utf-8 -*-


import copy
import networkx as nx
import data
from nodes import genes_classify, load_key_data

G = nx.DiGraph()


# G.add_nodes_from(data.nodes())


def gene_sort(name):
    return genes_classify()[name]


def add_pg_node():
    for n in data.nodes():
        try:
            flag = gene_sort(n)
            G.add_node(n, flag=flag)
        except:
            flag = 'phylum'
            G.add_node(n, flag=flag)


def add_sample_gene_node():
    for n in data.nodes():
        try:
            flag = gene_sort(n)
            G.add_node(n, flag=flag)
        except:
            pass
    for s in load_key_data()[1]:
        G.add_node(s, flag='sample')


def add_edge():
    for e1 in G.nodes:
        for e2 in G.nodes:
            if data.select(e1, e2) > 0.01:
                weight = 0
            else:
                weight = abs(data.select(e1, e2, flag=1))
            G.add_edge(e1, e2, weight=weight)


def add_edge_low():
    node_attr = {node: 0 for node in copy.deepcopy(G.nodes)}
    for e1 in list(G.nodes)[228:]:
        for e2 in list(G.nodes)[: 228]:
            if data.select(e1, e2) < 0.05:
                G.add_edge(e1, e2, weight=abs(data.select(e1, e2, flag=1)))
                node_attr[e1] = 1
                node_attr[e2] = 1
    for node in copy.deepcopy(G.nodes):
        if not node_attr[node]:
            G.remove_node(node)
    return G


if __name__ == '__main__':
    # nx.write_gml(add_edge_low(), 'C:\\users\\administrator\\desktop\\network\\network_phy_gen_0.05_del.gml')
    add_sample_gene_node()
