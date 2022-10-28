#!/usr/bin/python3

import requests
import base64
import os
import sys
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('URL')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
STACK = os.getenv('STACK')
ENVIRONMENT = os.getenv('ENVIRONMENT')
TAG = os.getenv('TAG')
URLREGISTRY =  os.getenv('URLREGISTRY')
USERNAMEREGISTRY = os.getenv('USERNAMEREGISTRY')
PASSWORDREGISTRY = os.getenv('PASSWORDREGISTRY')

if not URL:
    print('URL is not set. Quitting.')
    sys.exit(5)

if not USERNAME:
    print('USERNAME is not set. Quitting.')
    sys.exit(5)

if not PASSWORD:
    print('PASSWORD is not set. Quitting.')
    sys.exit(5)

if not STACK:
    print('STACK is not set. Quitting.')
    sys.exit(5)

if not ENVIRONMENT:
    ENVIRONMENT = []
else:
    ENVIRONMENT = ENVIRONMENT.split(',')

if not TAG:
    print('TAG is not set. Quitting.')
    sys.exit(5)

if not URLREGISTRY:
    print('URLREGISTRY is not set. Quitting.')
    sys.exit(5)

if not USERNAMEREGISTRY:
    print('USERNAMEREGISTRY is not set. Quitting.')
    sys.exit(5)

if not PASSWORDREGISTRY:
    print('PASSWORDREGISTRY is not set. Quitting.')
    sys.exit(5)


headers = {
        'Authorization': 'Basic {}'.format(
            base64.b64encode(
                '{username}:{password}'.format(
                    username=USERNAME,
                    password=PASSWORD).encode()
            ).decode()
        )
}

data_api = {
	"stack": STACK,
	"environment": ENVIRONMENT,
	"tag": TAG,
    "registry": URLREGISTRY,
    "username": USERNAMEREGISTRY,
    "password": PASSWORDREGISTRY
}

x = requests.post('{0}/login'.format(URL), headers=headers)
if x.status_code == 200:
    x_json = x.json()
    auth_token = x_json.get('x-access-tokens')
    hed = {'x-access-tokens': auth_token}

    y = requests.post('{0}/stack/update'.format(URL), headers=hed, json=data_api)
    y_json = y.json()
    status = y_json.get('status')
    print(y_json)
    if status or not status is None:
        sys.exit(0)
    else:
        sys.exit(5)
else:
    print({'status': False, 'message': 'error login'})
    sys.exit(5)