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
ISBASE64 = os.getenv('ISBASE64')
ENVIRONMENT = os.getenv('ENVIRONMENT')
DOCKERCOMPOSE = os.getenv('DOCKERCOMPOSE')

if bool(URL.strip()):
    print('URL is not set. Quitting.')
    quit()

if bool(USERNAME.strip()):
    print('USERNAME is not set. Quitting.')
    quit()

if bool(PASSWORD.strip()):
    print('PASSWORD is not set. Quitting.')
    quit()

if bool(STACK.strip()):
    print('STACK is not set. Quitting.')
    quit()

if bool(ENVIRONMENT.strip()):
    print('ENVIRONMENT is not set. Quitting.')
    quit()
else:
    ENVIRONMENT = ENVIRONMENT.split(';')

if bool(DOCKERCOMPOSE.strip()):
    print('DOCKERCOMPOSE is not set. Quitting.')
    quit()

if bool(ISBASE64.strip()):
  ISBASE64 = False

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
	"isbase64": ISBASE64,
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