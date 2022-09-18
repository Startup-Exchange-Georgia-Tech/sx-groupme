# Get modules/packages

import sys
from datetime import datetime, timezone
from creds import token

# Instantiate variables to be used throughout
from groupy.client import Client
client = Client.from_token(token)
groups = client.groups.list()
myuser = client.user.get_me()
chats = client.chats.list_all()
grouplist = list(groups.autopage())

grclient = Groupy('127.0.0.1:8990')
for user in grclient.users:
    print user
for permission in grclient.users.get('zorkian'):
    print permission