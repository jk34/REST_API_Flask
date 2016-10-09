import httplib2
import json

import sys
import codecs

google_api_key = ""
foursquare_client_id = "****************************"
foursquare_client_secret = "******************************"

def getGeocodeLocation(inputString):
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))

    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)

print getGeocodeLocation("Huntington Beach, California")
