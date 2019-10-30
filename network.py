# -*- coding: utf-8 -*-

"""
绘制network，生成gml图
"""

import networkx as nx
import nodes
import read_excel as rel


def draw_network():
    G = nx.DiGraph()
    sample_nodes = nodes.create_sample_node()
    gene_nodes = nodes.create_genes_node()
    phylum_nodes = nodes.create_phylum_node()

    for sample in sample_nodes:
        G.add_node(sample.name, flag='sample')

    for gene in gene_nodes:
        G.add_node(gene.name, flag=gene.sort)

    for phylum in phylum_nodes:
        G.add_node(phylum.name, flag='phylum')  

    for n_s in sample_nodes:
        for n_g in gene_nodes:
            # print(rel.get_cell_data(n_g.name, n_s.name))
            G.add_edge(n_s.name, n_g.name, weight=rel.get_cell_data(n_g.name, n_s.name))
        for n_p in phylum_nodes:
            G.add_edge(n_s.name, n_p.name, weight=nodes.phylum_cell_data(n_s.name, n_p.name))
    nx.write_gml(G, 'C:\\users\\administrator\\desktop\\network4.gml')


if __name__ == '__main__':
    draw_network()


