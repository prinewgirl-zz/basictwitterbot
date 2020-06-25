twitter app

Esse programa tem as seguintes funções:
    Fazer autenticação e autorização de usuário;
    Adicionar e remover hashtags que queremos acompanhar;
    Coletar de forma assíncrona mensagens publicadas no Twitter contendo as
    hashtags (dentro do limite da API);
    Listar as mensagens coletadas mostrando: mensagem, autor e data de
    publicação;
    Filtrar as mensagens listadas por hashtag.
    
    Os parâmetros de input e output são listados executando-se
    $ python3 twitterapp.py -h

Para instalar em um ambiente Linux, faça:

virtualenv venvtest -ppython3

. venvtest/bin/activate

pip install -r requirements.txt

$ python twitterapp.py <opções>

Para ajuda, digite:

$ python twitterapp.py -h
