import networkx as nx
import matplotlib.pyplot as plt

from functions import generate_random_parcels, generate_random_recipients, generate_road_matrix

random_parcels = generate_random_parcels(100)
for idx, parcel in enumerate(random_parcels, start=1):
    print(f"Parcel {idx}: Width - {parcel.width}, Weight - {parcel.weight}")

random_recipients = generate_random_recipients(10)

road_matrix = generate_road_matrix(random_recipients)

G = nx.Graph()
for (address1, address2), length in road_matrix.items():
    G.add_edge(address1, address2, length=length)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'length')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

if __name__ == '__main__':
    plt.show()
