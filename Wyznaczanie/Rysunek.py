import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

class Rysunek(object):
    
    def RysunekStart():
        
        G = nx.DiGraph()
        
        G.add_node("A", pos=(1,5))
        G.add_node("B", pos=(2,5))
        G.add_node("C", pos=(4,4))
        G.add_node("D", pos=(5,6))
        G.add_node("E", pos=(6,5))
        G.add_node("F", pos=(6,7))
        G.add_node("G", pos=(7,8))
        G.add_node("H", pos=(3,3))
        G.add_node("I", pos=(4,1))
        G.add_node("J", pos=(5,3))
        G.add_node("K", pos=(7,2))
        G.add_node("L", pos=(1,1))
       
        G.add_edge("A","B", weight=200, relation='linia')
        G.add_edge("B","C", weight=560, relation='linia')
        G.add_edge("C","D", weight=440, relation='linia')
        G.add_edge("D","E", weight=360, relation='linia')
        G.add_edge("E","K", weight=521, relation='linia')
        G.add_edge("K","G", weight=1210, relation='linia')
        G.add_edge("G","F", weight=320, relation='linia')
        G.add_edge("F","J", weight=792, relation='linia')
        G.add_edge("J","L", weight=2179, relation='linia')
        G.add_edge("L","I", weight=537, relation='linia')
        G.add_edge("I","H", weight=342, relation='linia')
        G.add_edge("H","A", weight=312, relation='linia')
        
        weight = nx.get_edge_attributes(G,'weight')
        pos = nx.get_node_attributes(G, 'pos')
        relation = nx.get_edge_attributes(G, 'relation')
        
        plt.figure()
        
        dic= { 'linia': 'blue'}
        
        nx.draw_networkx(G, pos, edge_color=[dic[x] for x in relation.values()])
        nx.draw_networkx_edge_labels(G,pos,edge_labels=weight)
