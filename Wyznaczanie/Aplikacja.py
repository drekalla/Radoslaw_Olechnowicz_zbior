
from Rysunek import Rysunek
from Vertex import Vertex
from Edge import Edge
from Algorytm import Algorytm

Rysunek.RysunekStart()

print("Dokąd chcesz się Udać? (Podaj nr wierzchołka np: A = 1...):")
Start = input()
Start = float(Start)
print("Gdzie się znajdujesz?:")
Koniec = input()
Koniec = float(Koniec)

A = Vertex("A")
B = Vertex("B")
C = Vertex("C")
D = Vertex("D")
E = Vertex("E")
F = Vertex("F")
G = Vertex("G")
H = Vertex("H")
I = Vertex("I")
J = Vertex("J")
K = Vertex("K")
L = Vertex("L")

def Poczatek(zmienna):
    switcher = {
        1: A,
        2: B,
        3: C,
        4: D,
        5: E,
        6: F,
        7: G,
        8: H,
        9: I,
        10: J,
        11: K,
        12: L,
    }
    return switcher.get(zmienna, "nothing")

edge1 = Edge(200,A,B)
edge2 = Edge(560,B,C)
edge3 = Edge(440,C,D)
edge4 = Edge(360,D,E)
edge5 = Edge(521,E,K)
edge6 = Edge(1210,K,G)
edge7 = Edge(320,G,F)
edge8 = Edge(792,F,J)
edge9 = Edge(2179,J,L)
edge10 = Edge(537,L,I)
edge11 = Edge(342,I,H)
edge12 = Edge(312,H,A)

A.adkacenciesList.append(edge1)
B.adkacenciesList.append(edge2)
C.adkacenciesList.append(edge3)
D.adkacenciesList.append(edge4)
E.adkacenciesList.append(edge5)
F.adkacenciesList.append(edge8)
G.adkacenciesList.append(edge7)
H.adkacenciesList.append(edge12)
I.adkacenciesList.append(edge11)
J.adkacenciesList.append(edge9)
K.adkacenciesList.append(edge6)
L.adkacenciesList.append(edge10)


vertexList = {A,B,C,D,E,F,G,H,I,J,K,L}



algorithm = Algorytm()
algorithm.ObliczNajkrotszaTrase(vertexList, Poczatek(Koniec))
algorithm.NajkrotszaDroga(Poczatek(Start))