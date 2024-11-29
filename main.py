"""
Diego Samperio Arce - A01662935
Franco Muñoz Ceballos - A01655440
Arely Yael Villatoro Amador - A01663303
Wilfrido Tovar Andrade - A01664769
"""

from FordFulkerson import fordFulkerson
from Kruskal import kruskalMST
from readFile import read_file

if __name__ == "__main__":
    # Leer número de nodos
    N = int(input("Enter the number of neighborhoods (N): "))

    # Leer la matriz de distancias
    distance_matrix = read_file('ActividadColaborativa2Algoritmos/distance_matrix.txt')

    # Leer la matriz de capacidades
    capacity_matrix = read_file('ActividadColaborativa2Algoritmos/capacity_matrix.txt')

    # Ejecutar Ford-Fulkerson y Kruskal para flujo y cableado máximo
    source = int(input("Enter the source node for maximum flow: "))
    sink = int(input("Enter the sink node for maximum flow: "))

    mst, mst_cost = kruskalMST(distance_matrix)
    print("\nOptimal way of wiring with fiber:")
    for edge in mst:
        print(f"({edge[0]},{edge[1]})")
    print(f"Total cost of the MST: {mst_cost}\n")
    max_flow = fordFulkerson(capacity_matrix, source, sink)
    print(f"\nMaximum information flow: {max_flow}")
