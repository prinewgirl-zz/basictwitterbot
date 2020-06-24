#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:21:43 2020

@author: Priscila
"""

import tweepy

class ManageTwitter:
    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, \
                 ACCESS_TOKEN_SECRET):
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth)
    def send(self, message):
        self.api.update_status(message)
    def erase(self, tweet_id):
        self.api.destroy_status(tweet_id)
    def search(self, text = None, language = 'None'):
        if language == None:
            result = tweepy.Cursor(self.api.search, q = text).items()
        else:
            result = tweepy.Cursor(self.api.search, q = text, 
                               lang = language).items()
        return result
    def reply(self, message, tweetid):
        self.api.update_status(message, in_reply_to_status_id = tweetid)
    def retweet(self, tweetid):
        self.api.retweet(tweetid)
    
