[![Maintainability](https://api.codeclimate.com/v1/badges/ecb041fb48b8fa903f2e/maintainability)](https://codeclimate.com/github/MandelaK/SendIT-API/maintainability)  [![Build Status](https://travis-ci.com/MandelaK/SendIT-API.svg?branch=ch-set-up-heroku-161863096)](https://travis-ci.com/MandelaK/SendIT-API) [![Coverage Status](https://coveralls.io/repos/github/MandelaK/SendIT-API/badge.svg)](https://coveralls.io/github/MandelaK/SendIT-API)
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


To install this repository
- clone it 
- create a virtual environment 
- do pip install -r requirements.txt in your virtual environment

To test on Postman:
- Open Postman and access the following endpoints:
  - `localost:/api/v1/parcels` - Send a POST request to this URL, but ensure your input is JSON and has the fieds for "sender",         "parcel_name", "user_id" <int>, recipient", "destination", "weight" <int must be greater than zero> and "pickup" present and filled with appropriate string, unless specified as int.
  - `localhost:/api/vi/parcels` - Send a GET request to this URL to get all parcels in the database
  - `localhost:/api/v1/parcels/<int:parcel_id>` - This endpint only accepts GET requests and returns a parcel with the specific ID passed
  - `localhost:/api/v1/users/<int:user_id>/parcels` - This endpoint only accepts GET requests and returns all parcels sent by the user whose ID was passed
  - `localhost:api/v1/parcels/<int:parcel_id>/cancel` - This endpoint accepts only PUT requests and allows you to cancel the destination. No input is needed from you, as long as the ID exists, the parcel order should be cancelled if it's in transit.


*How to test*
- As long as you've installed all dependencies, you can run `pytest` from terminal and it will show you which tests pass.


You can find the Heroku app published here - http://sendr-api.herokuapp.com/api/v1/parcels

The frontend for this application is available here - https://mandelak.github.io/SendIT/UI/static/html/index.html



The repository for the UI can be found here - https://github.com/MandelaK/SendIT


