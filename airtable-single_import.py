# imports
import argparse
import sys
import requests
import json
import re
import csv

# vars
omdb_apiKey = '4bc136e0'

# parsing arguments
movieInput = sys.argv[1]
movieYear = sys.argv[2]
myRating = sys.argv[3]

# cleaning up arguments, prepping for OMDB processing
myRating = str(myRating)
myRating = re.sub(r'\n', '', myRating)
fRating = float(myRating)
strPercRating = str(fRating)
cleanPercRating = re.sub(r'\.0', '', strPercRating)
movieName = re.sub(r'\s', '+', movieInput)
url = 'http://www.omdbapi.com/?type=movie&y=' + \
    movieYear + '&t=' + movieName + '&apikey=' + omdb_apiKey
r = requests.post(url)
data = r.json()

# setting variables from OMDB
movieTitle = data['Title']
movieYear = data['Year']
movieDirector = data['Director']
movieGenre = data['Genre']

# pushing to airtable
airURL = 'https://api.airtable.com/v0/appPs8NuOpz0Tjb8t/Movie%20Ratings'
airHeaders = {
    'Authorization': 'Bearer keyQkpTTG6cd7HiBB',
    'Content-Type': 'application/json'}
payload = {
    'fields': {
        'Title': movieTitle,
        'Year': movieYear,
        'Director': movieDirector,
        'Genre': movieGenre,
        'My Score': cleanPercRating + '%'}}
r = requests.post(airURL, headers=airHeaders, data=json.dumps(payload))