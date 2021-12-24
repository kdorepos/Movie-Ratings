# imports
import requests
import json
import re
import csv

# vars
omdb_apiKey = '4bc136e0'

# inputs
movieInput = input("Movie name? ")
movieYear = input("Movie year? ")
myRating = input("Your rating? ")

# starting loop
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
movieTitle = data['Title']
# movieTitle = re.sub(r'\'', '\\\'', movieTitle)
movieYear = data['Year']
movieDirector = data['Director']
movieGenre = data['Genre']
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
