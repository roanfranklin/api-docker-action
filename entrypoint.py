#!/usr/bin/python3

import requests
import base64
import os
import github_action_utils as gha_utils
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
    gha_utils.error('URL is not set. Quitting.')
    quit()

if not USERNAME:
    gha_utils.error('USERNAME is not set. Quitting.')
    quit()

if not PASSWORD:
    gha_utils.error('PASSWORD is not set. Quitting.')
    quit()

if not STACK:
    gha_utils.error('STACK is not set. Quitting.')
    quit()

if not ENVIRONMENT:
    gha_utils.error('ENVIRONMENT is not set. Quitting.')
    quit()
else:
    ENVIRONMENT = ENVIRONMENT.split(';')

if not DOCKERCOMPOSE:
    gha_utils.error('DOCKERCOMPOSE is not set. Quitting.')
    quit()

if not URLREGISTRY:
    gha_utils.error('URLREGISTRY is not set. Quitting.')
    quit()

if not USERNAMEREGISTRY:
    gha_utils.error('USERNAMEREGISTRY is not set. Quitting.')
    quit()

if not PASSWORDREGISTRY:
    gha_utils.error('PASSWORDREGISTRY is not set. Quitting.')
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