# REST_API_Flask

I ran Python scripts on Vagrant machine to startup web server listening on localhost port 5000. I then used Curl to send messages to this server and then receive HTTP responses of the requests.
I then used Curl to send requests to Google and Foursquare API and received responses. The Google Maps Geocoding API takes in a string representation of a location and returns the latitude and longitude coordinates of it. 
The Foursquare API finds a restaurant based on the latitude and longitude coordinates, city, and meal type of the user input
Also, ran Python scripts to send requests to the Google API and Foursquare API. 

The findARestaurant.py script takes in the mealtype and location as input, geocodes the location with Google API, passes in the returned latitude and longitude coordinates to the Foursquare API, and then parses the JSON response

The views.py script contains endpoints. One endpoint is a POST request that takes a string representation of a location and meal type, then geocodes the location, finds a nearby restaurant, and stores the entry in a database and returns the JSON object. One endpoint handles a GET request that returns all of the restaurants in your database in a JSON object. Another endpoint handles GET requests to return the name, ID, address, and image of a specific restaurant ID.
This script also handles the registration of new users. I can register a new user using Curl with username: Jerry and password: Udacity, and the server returns a response that the user has been registered.
It also lets registered users who log in with their correct password have accessed to protected areas
In views.py the user can request a token and it then handles tokens. 
It then contains the username, picture, email and password hash because those can be obtained with OAuth. I can then lookup users with their email addresses.  

The models.py stores password hashes, verifies passwords, the User model, and HTTP authorization. 

This app also has a client-side application that logs in wn with Google and receives an authentication code. The client then sends this code to my server which then communicates with Google to get a token. Then, I create my own token and send that to the client to authenticate with my application. 

Instead of creating a client-side application that sends the authorization code, there is the clientOAuth.html template in models.py that signs into Google and displays the authentication code

I learned about all of this as part of the "Designing RESTful APIs" course offered by Udacity


