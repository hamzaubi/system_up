from slack import WebClient
from slack.errors import SlackApiError
import socket

local_ip = socket.gethostbyname(socket.gethostname())
host_nane

client = WebClient('xoxb-1329250213920-1305440281394-rw2xT6QyYazapS3QqbecVXJF')
Welcome_message = "System is up and running" + "\n" + ("Current system ip is :{}").format(local_ip)

try:
    response = client.chat_postMessage(
        channel='#general',text=Welcome_message)
    assert response["message"]["text"] == Welcome_message
    print(Welcome_message)
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")
