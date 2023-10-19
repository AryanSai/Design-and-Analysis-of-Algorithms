import networkx

G = networkx.Graph()  #create an empty graph

# Adding some nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)
print(f"The number of nodes is: {G.number_of_nodes()}")

#adding some edges between the nodes already created
G.add_edge(1,2)
G.add_edge(3,2)

print(f"The number of edges is: {G.number_of_edges()}")

G.add_node(4)
G.add_node(5)

#Adding multiple edges at one time
G.add_edges_from([(4,2), (3,5), (5,4)])
print(f"The degree of node 2 is: {G.degree(2)}")

print(f"The list of nodes in the graph is: {G.nodes()}")
print(f"The list of edges in the graph is: {G.edges()}")

#removing a node
G.remove_node(4)

#removing an edge
G.remove_edge(1,2)

print(f"The list of nodes in the graph is: {G.nodes()}")
print(f"The list of edges in the graph is: {G.edges()}")