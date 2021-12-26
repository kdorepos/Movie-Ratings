# imports
import argparse
import requests
import json
import re
import csv

# vars
omdb_apiKey = '4bc136e0'

# starting process
parser = argparse.ArgumentParser(
    description='Parsing arguments for movie tracking'
)

parser.add_argument('-m', '--movie-name', metavar='movie_name', required=True)
parser.add_argument('-y', '--year', metavar='year', required=True)
parser.add_argument('-r', '--rating', metavar='rating', required=True)

args = parser.parse_args()

movieInput = args.movie_name
movieYear = args.year
myRating = args.rating

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