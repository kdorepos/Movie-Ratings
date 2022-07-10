# imports
import argparse
import sys
import requests
import json
import re
import csv

# parsing arguments
movieName = sys.argv[1]
url = sys.argv[2]

# pushing to airtable
airURL = 'https://api.airtable.com/v0/appVNst5E5cuYzbBM/Want?maxRecords=3&view=Grid%20view'
airHeaders = {
    'Authorization': 'Bearer keyQkpTTG6cd7HiBB',
    'Content-Type': 'application/json'}
payload = {
    'fields': {
        'Title': movieName,
        'Link': url}}
r = requests.post(airURL, headers=airHeaders, data=json.dumps(payload))