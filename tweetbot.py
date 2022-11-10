#!/usr/bin/python3
# -*- coding utf-8 -*-

# Original script (kept up to date): https://github.com/robincamille/bot-tutorial/blob/master/mybot.py

##### ##### ##### ##### #####
##### ##### ##### ##### ##### Housekeeping: do not edit.
##### ##### ##### ##### #####
from sre_constants import SRE_FLAG_MULTILINE
import tweepy as tp
import time
import random
import logging
import os
from datetime import datetime
from credentials import *
from tweetlist import *
from tweepy import OAuthHandler, API, TweepyException
auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tp.API(auth)
print('Authentication complete.')

##### ##### ##### ##### #####
##### ##### ##### ##### ##### Making sure that anything important is logged.
##### ##### ##### ##### #####
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)-12s - %(name)-12s - %(message)-12s', '%Y-%m-%d %H:%M:%S')
timestr = time.strftime("%Y%m%d")
os.chdir('/home/wednesday-addams/Documents/.Automation/Twitter Bots/Lesbian Wednesday Addams/Logs/')
handler = logging.FileHandler(f'{timestr}_LWA_Info.log')
handler.setFormatter(formatter)
logger.addHandler(handler)
##### Second os.chdir() just in case. I want the logs in the Logs subfolder.
os.chdir('/home/wednesday-addams/Documents/.Automation/Twitter Bots/Lesbian Wednesday Addams/')

##### ##### ##### ##### ##### 
##### ##### ##### ##### ##### Other things of note.
##### ##### ##### ##### ##### 

##### ##### Premiere of "Wednesday" on Netflix.
##### ##### Also, it's inspiration for this lesbian bot version.
wedn_date = "23/11/2022"
datefmt = "%d/%m/%Y"

wedn_prem = datetime.strptime(wedn_date, datefmt)
now = datetime.now()



##### ##### ##### ##### #####
##### ##### ##### ##### ##### Variables to be used.
##### ##### ##### ##### #####
##### ##### For some reason, when it was in the tweet() function, it was fine on GitHub, but
##### ##### when the exact same thing was on my Rasbperry Pi, it was not. Fucking thing kept
##### ##### going on about undeclared variables. Moving them outside the function seems to
##### ##### have sorted it. Let's hope it stands the test of time. It should to. It's a small
##### ##### script.
##### ##### \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
##### ##### /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
##### ##### Picks a number from the tweetlist and adds one.
##### ##### Initialises the total as a variable.
line = random.randint(0, len(tweetlist)-1)
twln = line + 1
twln_tot = len(tweetlist)
##### ##### Make sure it works for the conditional tweetlist too.
##### ##### Initialises variables for that too.
ct_line = random.randint(0, len(conditional_tweetlist)-1)
ct_twln = ct_line + 1
ct_twln_tot = len(conditional_tweetlist)

##### ##### ##### ##### #####
##### ##### ##### ##### ##### What the bot will tweet.
##### ##### ##### ##### #####
def tweet():
    ##### ##### Account for a situation in which an alternate tweet is published. For the first five tweets in the
    ##### ##### tweetlist (tweetlist[0] to tweetlist[4]), another thing will happen in certain circumstances.
    if twln <= 5:
        ##### ##### If "line" equals 0, which it will sometimes, then it needs to be tweeted in some capacity.
        if wedn_prem < now and line == 0:
            ##### ##### If November 23rd, 2022 (premiere date of Wednesday) has passed.
            if twln == 1:
                ##### ##### Make the random number attributed to "ct_line" equal that of "line".
                ct_line = line
                ##### ##### Tweet.
                api.update_status(conditional_tweetlist[line])
                ##### ##### Log it, both in the Termainal output and the log file. Make sure that the folder for the
                ##### ##### log files exist, or an error will be displayed saying the folder can not be found.
                print(f'{time.asctime()} - Conditional tweet {ct_twln} of {ct_twln_tot} posted: {conditional_tweetlist[ct_line]}')
                logger.info(f'Conditional Tweet {ct_twln} of {ct_twln_tot} posted: {conditional_tweetlist[ct_line]}')
                ##### ##### Exit the script.
                quit()
        else:
        ##### ### It will default to this once the until the show has premiered before permanently switching to
        ##### ### its conditional counterpart.
            if line == 0:
                ##### ##### Tweet.
                api.update_status(tweetlist[line])
                ##### ##### Log it, both in the Terminal output and the log file. Make sure that the folder for the
                ##### ##### log files exist, or an error will be displayed saying the folder can not be found.
                print(f'{time.asctime()} - Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
                logger.info(f'Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
                ##### ##### Exit the script.
                quit()
                
        ##### ##### If day-of-month is 31 and month is October.
        ##### ##### In a nutshell, if it's Halloween.
        if datetime.now().strftime("%d") == 31 and datetime.now().strftime("%B") == "October" and line == 1:
            ##### ##### If the second tweet in the tweetlist (tweetlist[1]) is chosen, but it's on Halloween,
            ##### ##### the second tweet in the conditional tweetlist (conditional_tweetlist[1]) will be selected
            ##### ##### instead.
            if twln == 2:
                ##### ##### Make the random number attributed to "ct_line" equal that of "line". This if statement will not run if
                ##### ##### line != 1, as twln will always equal line plus one.
                ct_line = line
                ##### ##### Tweet.
                api.update_status(conditional_tweetlist[line])
                ##### ##### Log it, both in the Termainal output and the log file. Make sure that the folder for the
                ##### ##### log files exist, or an error will be displayed saying the folder can not be found.
                print(f'{time.asctime()} - Conditional tweet {ct_twln} of {ct_twln_tot} posted: {conditional_tweetlist[ct_line]}')
                logger.info(f'Conditional Tweet {ct_twln} of {ct_twln_tot} posted: {conditional_tweetlist[ct_line]}')
                ##### ##### Exit the script.
                quit()
        else:
        ##### ### If "line" is equal to 1, but it is not Halloween...
            if line == 1:
                ##### ##### Tweet.
                api.update_status(tweetlist[line])
                ##### ##### Log it, both in the Terminal output and the log file. Make sure that the folder for the
                ##### ##### log files exist, or an error will be displayed saying the folder can not be found.
                print(f'{time.asctime()} - Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
                logger.info(f'Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
                ##### ##### Exit the script.
                quit()

        ##### ##### If month is October, but it's not Halloween.
        if datetime.now().strftime("%B") == "October" and datetime.now().strftime("%d") != 31 and line == 2:
            ##### ##### If the third tweet in the tweetlist is chosen, but it's also October, then the fourth tweet
            ##### ##### in the conditional tweetlist will be selected instead.
            if twln == 3:
                ##### ##### The value of "ct_line" will equal that of "line"
                ct_line = line
                ##### ##### Tweet.
                api.update_status(conditional_tweetlist[line])
                ##### ##### Log it.
                print(f'{time.asctime()} - Conditional tweet {ct_twln} of {ct_twln_tot} posted: {conditional_tweetlist[ct_line]}')
                logger.info(f'Conditional Tweet {ct_twln} of {ct_twln_tot} posted: {conditional_tweetlist[ct_line]}')
                ##### ##### And exit.
                quit()
        else:
        ##### ### If "line" is equal to 2, but it is October, but it's also not Halloween...
            if line == 2:
                ##### ##### Tweet.
                api.update_status(tweetlist[line])
                ##### ##### Log it, both in the Terminal output and the log file. Make sure that the folder for the
                ##### ##### log files exist, or an error will be displayed saying the folder can not be found.
                print(f'{time.asctime()} - Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
                logger.info(f'Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
                ##### ##### Exit the script.
                quit()

        ##### ##### If month is October.
        if datetime.now().strftime("%B") == "October" and line == 3:
            ##### ##### If the fourth tweet in the tweetlist is chosen, but it's also October, then the fourth tweet
            ##### ##### in the conditional tweetlist will be selected instead.
            if twln == 4:
                ##### ##### The value of "ct_line" will equal that of "line"
                ct_line = line
                ##### ##### Tweet.
                api.update_status(conditional_tweetlist[line])
                ##### ##### Log it.
                print(f'{time.asctime()} - Conditional tweet {ct_twln} of {ct_twln_tot} posted: {conditional_tweetlist[ct_line]}')
                logger.info(f'Conditional Tweet {ct_twln} of {ct_twln_tot} posted: {conditional_tweetlist[ct_line]}')
                ##### ##### And exit.
                quit()
        else:
        ##### ### If "line" is equal to 3, but it is not October...
            if line == 3:
                ##### ##### Tweet.
                api.update_status(tweetlist[line])
                ##### ##### Log it, both in the Terminal output and the log file. Make sure that the folder for the
                ##### ##### log files exist, or an error will be displayed saying the folder can not be found.
                print(f'{time.asctime()} - Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
                logger.info(f'Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
                ##### ##### Exit the script.
                quit()

        ##### ##### If day-of-week is Wednesday.
        if datetime.now().today().weekday() == 2 and line == 4:
            ##### ##### If the fifth tweet in the tweetlist is chosen, but it's also Wednesday, then the last tweet
            ##### ##### in the conditional tweetlist will be selected instead.
            if twln == 5:
                ##### ##### The value of "ct_line" will equal that of "line"
                ct_line = line
                ##### ##### Tweet
                api.update_status(conditional_tweetlist[line])
                ##### ##### Log it.
                print(f'{time.asctime()} - Conditional tweet {ct_twln} of {ct_twln_tot} posted: {conditional_tweetlist[ct_line]}')
                logger.info(f'Conditional Tweet {ct_twln} of {ct_twln_tot} posted: {conditional_tweetlist[ct_line]}')
                ##### ##### And exit.
                quit()
        else:
        ##### ### If "line" is equal to 4, but it is not Wednesday...
            if line == 4:
                ##### ##### Tweet.
                api.update_status(tweetlist[line])
                ##### ##### Log it, both in the Terminal output and the log file. Make sure that the folder for the
                ##### ##### log files exist, or an error will be displayed saying the folder can not be found.
                print(f'{time.asctime()} - Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
                logger.info(f'Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
                ##### ##### Exit the script.
                quit()

    else:
        ##### ##### If the value of twln is higher than that of len(conditional_tweetlist)
        ##### ##### Send a tweet.
        api.update_status(tweetlist[line])
        ##### ##### And log that motherfucker.
        print(f'{time.asctime()} - Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
        logger.info(f'Tweet {twln} of {twln_tot} posted: {tweetlist[line]}')
        ##### ##### And then exit.
        quit()


##### ##### Tweets, but also accounts for Tweepy errors and handles them accordingly.
##### #####
##### ##### However, that's making the bold assumption that the fucking thing will work and not throw
##### ##### an error saying it needs to be in an integer format or some shit. I've tried fixing this
##### ##### several times now and I'm not spamming tweets in the name of testing. If it misses an hour
##### ##### on the cronjob, I'll investigate and see what it says in "Errors.log". If it outputs something
##### ##### in the same format as the relevant if statement below, then we're golden and it's worked.
##### ##### The tweet will not have happened, but it will allow me to pinpoint the error and see where
##### ##### the problem is exactly, because in that regard, the error outputs from the crontab are about
##### ##### as useful to me as a concrete parachute. It just tells me where it stopped in the thing, not
##### ##### which tweet in the tweetlist is responsible for it.
try:
    tweet()
except TweepyException as err:
    int = err.args[0][0]
    if int == 186:
        ##### If the tweet is too long.
        print(f'{time.asctime()} - Error 186 - Tweet {twln} of {twln_tot}: Tweet needs to be shortened.')
        quit()
    if int == 187:
        ##### If the same tweet was published in the last 24 hours.
        print(f'{time.asctime()} - Error 187 - Tweet {twln} of {twln_tot}: Duplicate tweet detected. Same thing posted since this time yesterday.')
        quit()
    if int == 215:
        ##### If the authentication data is a bit iffy.
        print(f'{time.asctime()} - Error 215 - Bad authentication data. Please make sure your keys/credentials are correct and try again.')
        quit()
    if int == 401:
        ##### If someone accesses the thing when they shouldn't.
        print(f'{time.asctime()} - Error 401 - Unauthorized. Please make sure your keys/credentials are correct and try again.')
        quit()
