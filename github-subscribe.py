from slacker import Slacker
import os
import time

# Using a legacy slack token
slack = Slacker('your-slack-token')
channel_id = slack.channels.get_channel_id('github')

with open("sample-repolist.txt") as f:
   for line in f:
     text = line.rstrip("\n\r")
     ftext = "GithubOrganisation/" + text
     print(text)
     slack.chat.command(
          channel=channel_id,
          command="/github",
	  text='subscribe ' + ftext + ' commits:all reviews comments'
        )
     time.sleep(1)
#
