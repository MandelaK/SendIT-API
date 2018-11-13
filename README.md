[![Maintainability](https://api.codeclimate.com/v1/badges/ecb041fb48b8fa903f2e/maintainability)](https://codeclimate.com/github/MandelaK/SendIT-API/maintainability)  [![Build Status](https://travis-ci.com/MandelaK/SendIT-API.svg?branch=ch-set-up-heroku-161863096)](https://travis-ci.com/MandelaK/SendIT-API)  

# SendIT-API


SendIT is an application that allows users to create parcel deliveries and send them out. The users should be able to do the following:
- Create parcel delivery orders
- Users should be able to cancel delivery orders
- Change destination for deliveries in transit
- Admins should be able to change the current location of deliveries in transit
- The price of a delivery is determined by weight


This repository implements 



EndPoint                          Functionality

GET /parcels     -                 Fetch all parcel delivery orders

GET /parcels/<parcelId>       -    Fetch a specific parcel delivery order
  
GET /users/<userId>/parcels    -   Fetch all parcel delivery orders by a specific user
  
PUT /parcels/<parcelId>/cancel  -  Cancel the specific parcel delivery order

POST /parcels      -               Create a parcel delivery order


To install this repository, you can clone it, create a virtual environment and do pip install -r requirements.txt

You can find the Heroku app published here - http://sendr-api.herokuapp.com/api/v1/parcels

The frontend for this application is available here - https://mandelak.github.io/SendIT/UI/static/html/index.html

The repository for the UI can be found here - https://github.com/MandelaK/SendIT


