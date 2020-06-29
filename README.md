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

Modo de usar:

Primeiro, preencha o arquivo parametros.ini com os dados forecidos pelo twitter.

Exemplos comuns de uso:

Na linha de comando (terminal linux ou PowerShell, no caso do Windows) faça:

Para criar uma hashtag:

python twitterapp.py --cria '#hashtag'

Para listar uma hashtag por 1 minuto (60 segundos):

python twitterapp.py --filtra '#hashtag' 60

Para apagar todas as referências na sua timeline a uma hashtag:

python twitterapp.py --remove '#hashtag'