import csv
import pandas as pd

#esse código pega o CSV e transforma em DataFrame
#Eu peguei para exemplo os primeiros 50 csvs gerados no extrairdados.pv
#coloquei delimitadores entre as músicas de um artista e outro
#a primeira linha do full.csv contém a quantidade de artistas
#- artista; Example / aqui é onde começa o artista e mais uma linha do dataframe
#- fimartista; fim da lista de músicas do artista, que será colocada na outra coluna do dataframe
# cada linha tem duas colunas, a coluna do nome do artista e a outra a coluna da lista de músicas

main_arch = 'dataset/full.csv'
# Criar um DataFrame vazio para artistas
df_artistas = pd.DataFrame(columns=['nome', 'musicas'])

n_artist = []
n_musicas = []
quant = 0
quant_p = 0

with open(main_arch, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    primeira_linha = next(leitor_csv)
    quant = int(primeira_linha[0])
    print(quant)

for i in range(quant):
    musicas = []
    n_musicas.append(musicas)

# Abre o arquivo CSV em modo de leitura
with open(main_arch, 'r', encoding='utf-8') as arquivo_csv:
    # Cria um objeto leitor CSV
    leitor_csv = csv.reader(arquivo_csv)
    next(leitor_csv)
    # Itera sobre as linhas do arquivo CSV
    for linha in leitor_csv:
        # Processa cada linha como necessário
        nlinha = str(linha)
        nlinha = nlinha.strip('[\'').strip('\']')
        if '- artista; ' in nlinha:
            a = nlinha.split(';')
            artist = a[1]
            artist = artist.strip()
            n_artist.append(artist)
        elif '- fimartista;' in nlinha:
            if df_artistas.empty:
                df_artistas.loc[0] = [n_artist[quant_p], n_musicas[quant_p]]
            else:
                df_artistas.loc[df_artistas.index.max() + 1] = [n_artist[quant_p], n_musicas[quant_p]]
            quant_p += 1
        else:
            blist = nlinha.split(';";";')
            nan = 0
            n_song_n = ''
            n_song_art = []
            n_song_id = ''
            for x in blist:
                if nan==0:
                    n_song_n = x
                elif nan==1:
                    n_song_artx = x
                    n_song_artx = n_song_artx.split(';')
                    for i in n_song_artx:
                        i = i.strip().strip('"')
                        n_song_art.append(i)
                else:
                    n_song_id = x
                nan += 1
            nova_musica = {'nome': n_song_n, 'artistas': n_song_art, 'id': n_song_id}
            n_musicas[quant_p].append(nova_musica)

print("\nDataFrame de Artistas (após inserção):")
print(df_artistas)

# Caminho para o arquivo CSV de saída
caminho_saida = 'dataset/outputdataframe.csv'

# Salva o DataFrame em um arquivo CSV para testar se funcionou.
df_artistas.to_csv(caminho_saida, index=False, encoding='utf-8')

