from slackclient import SlackClient
import time

# Slack client for Web API requests
slack_client = SlackClient(SLACK_BOT_TOKEN)

def slack_connnect():
    return slack_client.rtm_connect()

def readRTM():
    while slack_client.server.connected is True:
        print(f'{slack_client.rtm_read()}')
        time.sleep(1)

def parseSlackInput(input, botID):
    botAID = "<@"+botID+">"
    if input and len(input) > 0:
        input = input[0]
        if 'text' in input and botAID in input['text']:
            user = input['user']
            message = input['text'].split(botAID)[1].strip(' ')
            channel = input['channel']
            return [str(user), str(message), str(channel)]
        else:
            return [None, None, None]

def getBotId(bot_user_name):
    user_list = slack_client.api_call("users.list")
    users = user_list["members"]
    for user in users:
        if 'name' in user and bot_user_name in user.get('name') and not user.get('deleted'):
            return user.get('id')

def postMessage(channel, message = None, attachments = None):
    return slack_client.api_call("chat.postMessage", channel = channel, text = message, as_user = True, attachments = attachments)