from slack import WebClient
from slack.errors import SlackApiError
import socket
import os

local_ip = socket.gethostbyname(socket.gethostname())
host_name = socket.gethostname()
logged_user = os.getlogin()

client = WebClient('xoxb-1329250213920-1305440281394-7PSSOI98lp7XPVIDVEwwDeLs')
ssh_address = "ssh:"+ logged_user+"@"+local_ip
welcome_message = "System is up and running" + '\n' + ("Current local ip is :{} , \nLogged  in user is :{}").format(local_ip,logged_user)
welcome_message = welcome_message + '\n' + ssh_address

try:
    response = client.chat_postMessage(
        channel='#general',text=welcome_message)
    assert response["message"]["text"] == welcome_message
    print(welcome_message)
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")
