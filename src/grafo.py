import networkx as nx
import matplotlib.pyplot as plt
from separando import df_artistas

# Cria um grafo direcionado
G = nx.DiGraph()

# Adiciona nós ao grafo (artistas)
for _, row in df_artistas.iterrows():
    G.add_node(row['nome'])

# Adiciona arestas ao grafo (relação entre artistas e músicas)
for _, row in df_artistas.iterrows():
    nome_artista = row['nome']
    for musica in row['musicas']:
        # Ajuste o nome da música para evitar caracteres especiais
        nome_musica = musica['nome'].replace('$', 's').replace('(', '').replace(')', '').replace('.', '').replace(',', '')
        for artista_2 in musica['artistas']:
            if artista_2 != nome_artista:
                for _, row in df_artistas.iterrows():
                    if artista_2 == row['nome']:
                        nome_artista = nome_artista.replace('$', 's').replace('(', '').replace(')', '').replace('.', '').replace(',', '')
                        artista_2 = artista_2.replace('$', 's').replace('(', '').replace(')', '').replace('.', '').replace(',', '')
                        G.add_edge(nome_artista, artista_2, musica=nome_musica)

newit = 1

with open('outputgrafo.txt', 'w', encoding='utf-8') as newfile:
    for u, v, data in G.edges(data=True):
        newfile.write(f'{newit} - Aresta entre artistas "{u}" e "{v}", Música: "{data["musica"]}"\n')
        print(f'{newit} - Aresta entre artistas "{u}" e "{v}", Música: "{data["musica"]}"')
        newit += 1

# Desenha o grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_size=8, node_size=700, font_color='black', font_weight='bold', arrowsize=10)

# Adiciona os rótulos das arestas (nomes das músicas)
edge_labels = {(u, v): data['musica'] for u, v, data in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', label_pos=0.5, font_size=6)

plt.show()