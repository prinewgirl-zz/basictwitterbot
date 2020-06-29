#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esse programa tem as seguintes funções:
    Fazer autenticação e autorização de usuário;
    Adicionar e remover hashtags que queremos acompanhar;
    Coletar de forma assíncrona mensagens publicadas no Twitter contendo as
    hashtags (dentro do limite da API);
    Listar as mensagens coletadas mostrando: mensagem, autor e data de
    publicação;
    Filtrar as mensagens listadas por hashtag.
    
    Os parâmetros de input e output são listados executando-se
    $ python3 botapp.py -h
"""

import argparse
import configparser
import os
from lib import TwitterModule
from lib import ManipulaExcecoes
from tweepy import error
import sys 

###############################################################################
## a partir de um arquivo pré-definido chamado parametros.ini, lê configurações
## básicas como CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN e 
##  ACCESS_TOKEN_SECRET
###############################################################################

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(),"parametros.ini"))
consumer_key = config.get("Geral","CONSUMER_KEY")
consumer_secret = config.get("Geral","CONSUMER_SECRET")
acess_token = config.get("Geral","ACESS_TOKEN")
acess_token_secret = config.get("Geral","ACESS_TOKEN_SECRET")
user = config.get("Geral","USERNAME")

###############################################################################
## Configura os argumentos passados para a linha de comando
## utiliza o pacote configparser para isso
###############################################################################

parser = argparse.ArgumentParser()
parser.add_argument('--adiciona', help='Adiciona uma hashtag', 
                    metavar='<hashtag>',default=None)
parser.add_argument('--remove', help='Remove uma hashtag', 
                    metavar='<hashtag>',default=None)
parser.add_argument('--filtra', help='Filtra uma hashtag especificando  a \
                    hashtag e o tempo', 
                    metavar='<arg>',default=None, nargs=2)
args = parser.parse_args()

def cria_hashtag(texto):
    '''essa função recebe um texto, não retorna nada apenas envia o tweet'''
    #verifica se o texto contém no máximo 280 caracteres
    if len(texto) > 280:
        raise ManipulaExcecoes.LengthError("No. de caracteres excedido")
    else:
        if '#' in texto:
            bot.send(texto)
        else:
            raise ManipulaExcecoes.HashtagNotFound("não contém hashtag")

def rm_hashtag(hashtag):
    '''essa função recebe uma hashtag e deleta todos os tweets feitos
    pelo usuário a usando'''
    if '#' in hashtag:
        bot.erase_all(hashtag)
    else:
        raise ManipulaExcecoes.HashtagNotFound ("não contém hashtag")

def filtra(hashtag, tempo):
    '''essa função recebe uma hashtag e filtra todos os tweets que estão 
    sendo feitos a partir dela'''
    try:
        bot.stream(hashtag, tempo)
    except KeyboardInterrupt:
        sys.exit()

try:    

    bot = TwitterModule.ManageTwitter(consumer_key,consumer_secret,\
                                          acess_token, acess_token_secret)
    bot.verify()
    
    if args.adiciona is not None:
        cria_hashtag(args.adiciona)
    if args.remove is not None:
        rm_hashtag(args.remove)
    if args.filtra is not None:
        filtra(args.filtra[0], int(args.filtra[1]))

except ManipulaExcecoes.LengthError as tamexce:
    sys.stderr.write(tamexce)
    sys.exit()
except ManipulaExcecoes.HashtagNotFound as hashnot:
    sys.stderr.write(hashnot)
    sys.exit()
except error.TweepError as error:
    print("Problema com a API do bot")
    sys.stderr.write(error)
    sys.exit()
except KeyboardInterrupt:
    sys.exit()
