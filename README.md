# Trabalho-Final-AEDS-II
Um trabalho a respeito das Conexões entre artistas por meio de suas parcerias e colaborações musicais. Feito em Python.

O ranking de artistas mais reproduzidos no Spotify foi obtido nesse link:
https://chartmasters.org/most-streamed-artists-ever-on-spotify/

No dataset está o código usado para acessar a API do Spotify e obter os dados específicos para a proposta do meu trabalho.
Foi colocado o txt com os Top 250 artistas, mas vale lembrar a quem quiser reproduzir o teste e obter novos dados:
O servidor API do Spotify possui um limite de requisições, portanto no exemplo dessa implementação, o usuário consegue obter dados de no máximo 70 artistas por conta.
Alguns artistas não serão usados na parte do grafo por não possuírem músicas em colaboração com outros artistas.

O CSV usado na implementação que encontra o dataframe que é usado para aplicação do algoritmo de grafos, foi uma junção dos 100 artistas mais reproduzidos.
Foram colocadas delimitações padronizadas no arquivo CSV para facilitar na execução do código.

Para testar o programa, basta executar o arquivo grafo.py e garanta que os arquivos dataframe.py e full.csv estejam na mesma pasta. No dataset tem 3 arquivos full csv (de 50, 100 e 150), o full.csv que está na pasta src é o que foi utilizado nos resultados do artigo.

# Arquivos 'dataset'

- pasta 'csvspotify': pasta com os arquivos csvs isolados de cada artista.
- artistas.txt : arquivo usado na extração de dados dos artistas. pela limitação de acesso ao servidor, a cada execução do código peguei partes de 30 artistas.
- Top250Artists.txt : arquivo contendo todos os artistas do ranking que considerei a partir da data de acesso do site.
- extrairdados.py : arquivo para extrair os dados da API do spotify e retornar cada csv separadamente.
- full.csv : arquivo usado pra montar o dataframe a ser executado em src/dataframe.py, full100.csv e full150.csv tem o mesmo propósito, porém quantidade de artistas diferentes.
- outputdataframe.csv : arquivo de resultado da execução do dataframe.

# Arquivos 'src'

- dataframe.py : arquivo que pega o csv com os artistas e suas listas de música e transforma em dataframe que será utilizado na montagem do grafo.
- grafo.py: pega o dataframe e constrói o grafo, e apresenta os cliques de maior quantidade de vértices e top 20 maiores colaborações entre 2 artistas.
