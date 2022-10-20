#!/usr/bin/python3

import requests
import base64
import os
#import github_action_utils as gha_utils
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('URL')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
STACK = os.getenv('STACK')
ENVIRONMENT = os.getenv('ENVIRONMENT')
DOCKERCOMPOSE = os.getenv('DOCKERCOMPOSE')
URLREGISTRY =  os.getenv('URLREGISTRY')
USERNAMEREGISTRY = os.getenv('USERNAMEREGISTRY')
PASSWORDREGISTRY = os.getenv('PASSWORDREGISTRY')

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

if not URLREGISTRY:
    print('URLREGISTRY is not set. Quitting.')
    quit()

if not USERNAMEREGISTRY:
    print('USERNAMEREGISTRY is not set. Quitting.')
    quit()

if not PASSWORDREGISTRY:
    print('PASSWORDREGISTRY is not set. Quitting.')
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
    "data": DOCKERCOMPOSE,
    "registry": URLREGISTRY,
    "username": USERNAMEREGISTRY,
    "password": PASSWORDREGISTRY
}

x = requests.post('{0}/login'.format(URL), headers=headers)
if x.status_code == 200:
    x_json = x.json()
    auth_token = x_json.get('token')
    hed = {'x-access-tokens': auth_token}

    y = requests.post('{0}/stack/updatev2'.format(URL), headers=hed, json=data_api)
    print(y.json())