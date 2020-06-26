#!/usr/bin/env python2

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:21:43 2020

@author: Priscila
"""

import tweepy

class ManageTwitter:
    '''This class manage tweepy API making it easy for the user'''
    
    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, \
                 ACCESS_TOKEN_SECRET):
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth,wait_on_rate_limit=True,
                              wait_on_rate_limit_notify=True)
#        self.streaming = self.MyStreamListener()
        
    def send(self, message):
        '''Sends a simple message.
        Input: message (string)
        '''
        self.api.update_status(message)
    def erase(self, tweet_id):
        '''Erases a single message
        Input: message ID (string)
        '''
        self.api.destroy_status(tweet_id)
    def erase_all(self,pattern):
        '''Erases a bunch of messages with a pattern
        Input: pattern (string)
        '''
        for status in tweepy.Cursor(self.api.user_timeline).items():
            if pattern in status.text:
                self.api.destroy_status(status.id)
    def search(self,text, items = 10):
        '''Searchs for some text in tweets
        Input: text, items (optional)
        Output: tweets that match
        '''
        result = tweepy.Cursor(self.api.search, q=text).items(items)
        return result
    def reply(self, message, tweetid):
        '''Reply a message by a certain user
        Input: message (string), tweetid (string) 
        '''
        self.api.update_status(message, in_reply_to_status_id = tweetid)
    def retweet(self, tweetid):
        '''Retweet a message by a certain user
        Input: tweetid (string)
        '''
        self.api.retweet(tweetid)
        
    def verify(self):
        '''
        Verify if the credentials are ok. 
        Raise an exception if not
        '''
        self.api.verify_credentials()
    def stream(self,message):
        streaming = self.MyStreamListener()
        streaming.on_status(message, self.api)
        
class MyStreamListener(tweepy.StreamListener):
    def __init__(self,message, api):
        self.api = api
        self.myStream = tweepy.Stream(auth = api.auth, 
                                      listener=myStreamListener)