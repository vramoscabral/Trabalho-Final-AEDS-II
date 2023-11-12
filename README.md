# Trabalho-Final-AEDS-II
Um trabalho a respeito das Conexões entre artistas por meio de suas parcerias e colaborações musicais.

O ranking de artistas mais reproduzidos no Spotify foi obtido nesse link:
https://chartmasters.org/most-streamed-artists-ever-on-spotify/

No dataset está o código usado para acessar a API do Spotify e obter os dados específicos para a proposta do meu trabalho.
Foi colocado o txt com os Top 250 artistas, mas vale lembrar a quem quiser reproduzir o teste e obter novos dados:
O servidor API do Spotify possui um limite de requisições, portanto no exemplo dessa implementação, o usuário consegue obter dados de no máximo 70 artistas por conta.

O CSV usado na implementação que encontra o dataframe que é usado para aplicação do algoritmo de grafos, inicialmente para testes, foi uma junção dos 50 artistas mais reproduzidos.
Foram colocadas delimitações padronizadas no arquivo CSV para facilitar na execução do código.
