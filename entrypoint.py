#!/usr/bin/python3

import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('URL')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
STACK = os.getenv('STACK')
ENVIRONMENT = os.getenv('ENVIRONMENT')
DOCKERCOMPOSE = os.getenv('DOCKERCOMPOSE')

if not URL:
    print('URL is not set. Quitting.')
    quit()

if not USERNAME:
    print('USERNAME is not set. Quitting.')
    quit()

if not PASSWORD:
    print('PASSWORD is not set. Quitting.')
    quit()

if not STACK:
    print('STACK is not set. Quitting.')
    quit()

if not ENVIRONMENT:
    print('ENVIRONMENT is not set. Quitting.')
    quit()
else:
    ENVIRONMENT = ENVIRONMENT.split(';')

if not DOCKERCOMPOSE:
    print('DOCKERCOMPOSE is not set. Quitting.')
    quit()


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
	"data": DOCKERCOMPOSE
}

x = requests.post('{0}/login'.format(URL), headers=headers)
if x.status_code == 200:
    x_json = x.json()
    auth_token = x_json.get('token')
    hed = {'x-access-tokens': auth_token}

    y = requests.post('{0}/stack/updatev2'.format(URL), headers=hed, json=data_api)
    print(y.json())