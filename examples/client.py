#!/usr/bin/env python

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from accepton import Client

API_KEY = 'skey_be064297e7b2db4b6ce5928e8dcad582'

accepton = Client(api_key=API_KEY, environment='development')
token = accepton.create_token(amount=1099, application_fee=99, currency='cad',
                              description='Test charge')

print(token)
