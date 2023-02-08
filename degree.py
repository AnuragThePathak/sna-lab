import matplotlib.pyplot as plt
import networkx as nx
import csv

G = nx.Graph()
with open('./dolphins.csv', 'r') as f:
	data = csv.reader(f)
	for row in data:
		G.add_edge(row[0], row[1])


deg_centrality = nx.degree_centrality(G)
print(deg_centrality)

plt.figure(figsize=(13, 8))
nx.draw_networkx(G, with_labels= True)
plt.show()