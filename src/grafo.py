import networkx as nx
import matplotlib.pyplot as plt
from dataframe import df_artistas

# Cria um grafo direcionado
G = nx.DiGraph()

# Adiciona nós ao grafo (artistas)
for _, row in df_artistas.iterrows():
    nome_artista = row['nome'].strip()  # Remover espaços extras no início e no final do nome
    G.add_node(nome_artista)

# Adiciona arestas ao grafo (relação entre artistas e músicas)
for _, row in df_artistas.iterrows():
    nome_artista = row['nome'].strip()
    for musica in row['musicas']:
        # Ajuste o nome da música para evitar caracteres especiais
        nome_musica = musica['nome'].replace('$', 's').replace('(', '').replace(')', '').replace('.', '').replace(',', '')
        for artista_2 in musica['artistas']:
            artista_2 = artista_2.strip()
            if artista_2 != nome_artista:
                for _, row in df_artistas.iterrows():
                    if artista_2 == row['nome'].strip():
                        nome_artista = nome_artista.replace('$', 's').replace('(', '').replace(')', '').replace('.', '').replace(',', '')
                        artista_2 = artista_2.replace('$', 's').replace('(', '').replace(')', '').replace('.', '').replace(',', '')
                        
                        # Verifica se a aresta já existe
                        if G.has_edge(nome_artista, artista_2):
                            G[nome_artista][artista_2]['musica'] += 1
                        else:
                            G.add_edge(nome_artista, artista_2, musica=1)  # Peso inicial é 1

newit = 1

with open('outputgrafo.txt', 'w', encoding='utf-8') as newfile:
    for u, v, data in G.edges(data=True):
        newfile.write(f'{newit} - Aresta entre artistas "{u}" e "{v}", número de contribuições: "{data["musica"]}"\n')
        #print(f'{newit} - Aresta entre artistas "{u}" e "{v}", contribuição número: "{data["musica"]}"')
        newit += 1

# Desenha o grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_size=8, node_size=700, font_color='black', font_weight='bold', arrowsize=10)

# Adiciona os rótulos das arestas (contagem de ocorrências de músicas)
edge_labels = {(u, v): data['musica'] for u, v, data in G.edges(data=True) if 'musica' in data}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', label_pos=0.5, font_size=6)

# Encontrar cliques de peso máximo no grafo não direcionado
G_undirected = G.to_undirected()
cliques = list(nx.find_cliques(G_undirected))

# Filtrar cliques onde existem arestas entre todos os artistas
cliques_validos = [
    (x, sum(G[u][v].get('musica', 0) for u, v in zip(x, x[1:])))
    for x in cliques
    if all(G.has_edge(u, v) for u, v in zip(x, x[1:]))
]

# Classificar os cliques válidos com base na soma total de músicas em ordem decrescente
cliques_ordenados = sorted(cliques_validos, key=lambda x: x[1], reverse=True)

# Imprimir os 10 cliques de maior valor
for i, (clique, soma) in enumerate(cliques_ordenados[:10], start=1):
    print(f'{i}. Clique: {clique}, Soma total: {soma}')

    # Imprimir o peso de cada aresta no clique
    for u, v in zip(clique, clique[1:]):
        peso_aresta = G[u][v].get('musica', 0)
        print(f'   Aresta entre artistas "{u}" e "{v}", Peso: {peso_aresta}')

# Exibir os cliques de maior valor
print(f'Total de cliques: {len(cliques_validos)}')

# Obter as 20 maiores arestas com base no peso
maiores_arestas = sorted(G.edges(data=True), key=lambda x: x[2].get('musica', 0), reverse=True)[:20]

newit = 1

print('Maiores contribuições entre 2 artistas:\n')
# Imprimir as 20 maiores arestas
for newit, (u, v, data) in enumerate(maiores_arestas, start=1):
    peso_aresta = data.get('musica', 0)
    print(f'{newit} - Aresta entre artistas "{u}" e "{v}", número de contribuições: "{peso_aresta}"')

plt.show()
