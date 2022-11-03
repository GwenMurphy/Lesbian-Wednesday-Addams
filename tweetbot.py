#!/usr/bin/python3
# -*- coding utf-8 -*-

# Original script (kept up to date): https://github.com/robincamille/bot-tutorial/blob/master/mybot.py


##### ##### ##### ##### ##### Housekeeping: do not edit.
from sre_constants import SRE_FLAG_MULTILINE
import tweepy as tp
import time
import random
import logging
import os
import datetime
from credentials import *
from tweetlist import *
auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tp.API(auth)
print('Authentication complete.')

##### ##### ##### ##### ##### Making sure that anything important is logged.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)-12s - %(name)-12s - %(message)-12s', '%Y-%m-%d %H:%M:%S')
timestr = time.strftime("%Y%m%d")
os.chdir('/home/wednesday-addams/Documents/.Automation/Twitter Bots/Lesbian Wednesday Addams/')
handler = logging.FileHandler(f'{timestr}_LWA_Info.log')
handler.setFormatter(formatter)
logger.addHandler(handler)

##### ##### ##### ##### ##### What the bot will tweet.
def tweet():
    ##### ##### Picks a number from the main tweetlist and adds one to the number.
    line = random.randint(0, len(tweetlist)-1)
    twln = line + 1
    twln_tot = len(tweetlist)

    ##### ##### Make it work for the conditional tweetlist too.
    ct_line = random.randint(0, len(conditional_tweetlist)-1)
    ct_twln = ct_line + 1
    ct_twln_tot  = len(conditional_tweetlist)

    ##### ##### And the song list
    sl_line = random.randint(0, len(song_list)-1)
    sl_twln = sl_line + 1
    sl_twln_tot = len(song_list)

    ##### ##### And the streetfood list
    sf_line = random.randint(0, len(streetfood)-1)
    sf_twln = sl_line + 1
    sf_twln_tot = len(streetfood)

    ##### ##### And the celebrity crush tweetlist
    cb_line = random.randint(0, len(celeb)-1)
    cb_twln = cb_line + 1
    cb_twln_tot = len(celeb)

    ##### ##### Account for any situation in which an alternate tweet is published.
    if twln < 10:
        ##### ##### Chooses the tweet from the other list.
        ##### Is it Halloween?
        if datetime.datetime.now().strftime("%d") == 31 and datetime.datetime.now().strftime("%B") == "October" and twln == 2:
            ct_twln = 2
            api.update_status(conditional_tweetlist[ct_twln-1])
            print(f'Conditional Tweet {ct_twln} of {ct_twln_tot} posted: {conditional_tweetlist[ct_line]}')
            logger.info(f'Conditional Tweet {ct_twln} of {ct_twln_tot} posted: {conditional_tweetlist[ct_line]}')
            quit()
        
        ##### Is it October?
        elif datetime.datetime.now().strftime("%B") == "October" and twln == 4:
            ct_twln = 4
            api.update_status(conditional_tweetlist[ct_twln-1])
            print(f'Conditional Tweet {ct_twln} of {ct_twln_tot} posted: {conditional_tweetlist[ct_line]}')
            logger.info(f'Conditional Tweet {ct_twln} of {ct_twln_tot} posted: {conditional_tweetlist[ct_line]}')
            quit()
        
        ##### Is it Wednesday?
        elif datetime.datetime.today().weekday() == 2:
            ct_twln = 5
            api.update_status(conditional_tweetlist[ct_twln-1])
            print(f'Conditional Tweet {ct_twln} of {ct_twln_tot} posted: {conditional_tweetlist[ct_line]}')
            logger.info(f'Conditional Tweet {ct_twln} of {ct_twln_tot} posted: {conditional_tweetlist[ct_line]}')
            quit()
        
        ##### Is there a song stuck in Wednesday's head?
        elif twln == 6 or twln == 7:
            sl_twln = sl_line
            api.update_status(tweetlist[line])
            print(f'Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
            logger.info(f'Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
            quit()

        ##### Is Wednesday thinking about street food?
        elif twln == 8 or twln == 9:
            sf_twln = sf_line
            api.update_status(tweetlist[line])
            print(f'Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
            logger.info(f'Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
            quit()

        ##### Is Wednesday thinking about a celebrity crush?
        elif twln == 10:
            cb_twln = cb_line
            api.update_status(tweetlist[line])
            print(f'Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
            logger.info(f'Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
            quit()

        api.update_status(conditional_tweetlist[line])
        print(f'Conditional Tweet {ct_twln} of {ct_twln_tot} posted: {conditional_tweetlist[ct_line]}')
        logger.info(f'Conditional Tweet {ct_twln} of {ct_twln_tot} posted: {conditional_tweetlist[ct_line]}')
        quit()
    else:
        ##### Comment this out during testing.
        api.update_status(tweetlist[line])
        ##### Print to the command line.
        print(f'Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
        ##### Print to the log file too.
        logger.info(f'Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
        quit()

    
    ##### ##### Comment this out when doing testing. Don't want to post tweets outside the schedule set by the cronjob.
    # api.update_status(tweetlist[line])

    ##### ##### Prints the tweet to the command line along w/ its position in the tweet list.
    # print(f'Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
    
    ##### ##### Logs it to the logging file so that it can be checked anytime. Helpful should anything go wrong, which it shouldn't.
    # logger.info(f'Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')

# Does exactly what you think it does.
tweet()
