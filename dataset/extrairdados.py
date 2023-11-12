import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import csv
import os

output_folder = 'csvspotify'
artists_file = 'artistas.txt'  # Nome do arquivo com a lista de artistas

# Substitua estas variáveis com suas credenciais
client_id = 'SEU CLIENTE ID'
client_secret = 'SEU CLIENT SECRET'
redirect_uri = 'http://localhost:8888/callback'
#essa parte é fundamental pra que você consiga acessar o API do spotify e obter os dados
#com sua conta no spotify, entre no spotify para developers
#crie um app no dashboard, e nas configurações do app vão estar os IDs q vc precisa.

# Configuração da autenticação usando o fluxo de autorização
client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# autenticação pra primeira execução
#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
 #                                              client_secret=client_secret,
  #                                             redirect_uri=redirect_uri,
   #                                            scope='user-library-read',
    #                                           cache_path=".cache"))

# Ler a lista de artistas do arquivo
with open(artists_file, 'r', encoding='utf-8') as file:
    artist_names = [line.strip() for line in file]

#o indicador da posição do artista no ranking.
artint = 171

# Iterar sobre a lista de artistas
for artist_name in artist_names:
    # Obtenha o ID do artista
    results = sp.search(q=f'artist:{artist_name}', type='artist')
    artist_id = results['artists']['items'][0]['id'] if results['artists']['items'] else None
    artist_name = artist_name.replace('/', '_') 

    # Se o artista for encontrado, obtenha todas as músicas
    if artist_id:
        all_tracks = []

        # Pagine através dos álbuns do artista, incluindo singles
        offset = 0
        limit = 50
        while True:
            albums = sp.artist_albums(artist_id, album_type='album,single', limit=limit, offset=offset)

            # Se não houver mais álbuns, saia do loop
            if not albums['items']:
                break

            # Para cada álbum ou single, obtenha as faixas
            for album in albums['items']:
                album_id = album['id']
                tracks = sp.album_tracks(album_id)['items']
                all_tracks.extend(tracks)

            # Aumente o offset para a próxima página
            offset += limit

        # Prepare dados para CSV
        csv_data = [['Nome da Música', 'Artistas', 'ID da Música']]

        # salva no csv apenas músicas de parceria (feat), com mais de um artista.
        for track in all_tracks:
            song_name = track['name']
            song_id = track['id']
            artists = [artist['name'] for artist in track['artists']]

            if len(artists) > 1:
                csv_data.append([song_name, ';', '; '.join(artists), ';', song_id])

        if artint < 10:
            artint = str(artint)
            artint = '00' + artint
        elif artint < 100:
            artint = str(artint)
            artint = '0' + artint

        # Escreva para CSV
        csv_filename = os.path.join(output_folder, f'{artint}_{artist_name}_songs.csv')
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            csv_writer.writerows(csv_data)

        print(f"Arquivo CSV '{csv_filename}' criado com sucesso para o artista '{artist_name}'.")
        artint = int(artint)
        artint += 1
    else:
        print(f"Artista '{artist_name}' não encontrado.")

print("Operação de extração de dados encerrada.")

# https://chartmasters.org/most-streamed-artists-ever-on-spotify/