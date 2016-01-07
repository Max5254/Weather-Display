import urllib2
import json
WeatherFile = "weather.txt"

url = 'http://api.wunderground.com/api/132e68feddbba074/geolookup/conditions/q/NY/Trumansburg.json'
response = urllib2.urlopen(url)

fh = open(WeatherFile,'w')

fh.write(response.read())
fh.close()

