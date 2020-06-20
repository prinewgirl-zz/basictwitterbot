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
"""

import configparser
import os


###############################################################################
## a partir de um arquivo pré-definido chamado parametros.ini, lê configurações
## básicas como CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN e 
##  ACCESS_TOKEN_SECRET
###############################################################################

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(),"parameters.ini"))
consumer_key    = config.get("General","CONSUMER_KEY")
consumer_secret = config.get("General","CONSUMER_SECRET")
access_token = config.get("General","ACESS_TOKEN")
access_token_secret = config.get("General","ACESS_TOKEN_SECRET")

