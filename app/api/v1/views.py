from flask_restful import Resource
from .models import Parcel
from flask import request

parcel_obj = Parcel()


class GenericParcel(Resource):
    """This class contains generic parcels without
    any specificity."""

    def get(self):
        parcels = parcel_obj.get_all()
        return parcels, 200

    def post(self):
        """This method is for adding a delivery to our database."""

        data = request.get_json()
        sender = data['sender']
        user_id = data['user_id']
        recipient = data['recipient']
        destination = data['destination']
        weight = data['weight']
        pickup = data['pickup']

        response = parcel_obj.add_parcel(sender, user_id, recipient,
                                         destination, weight, pickup)
        if response == 201:
            return {"Success": "Successfully added your delivery"}, 201


class SpecificParcel(Resource):
    """This class contains methods for manipulating a specific parcel"""

    def get(self, id):
        """This method should return a parcel if we are sent it's id"""
        response = parcel_obj.get_parcel(id)
        if response == 404:
            return {"message": "Parcel does not exist"}
        return response, 200

        # for parcel in parcels:
        #     if parcel['id'] == id:
        #         #change the destination
        #         pass
        #     else:
        #         return{"message" : "No such delivery was found"}, 400


class User(Resource):
    """This class represents the user and what actions they can do to their
    parcels"""

    def get(self, user_id):
        """This method gets all deliveries sent by a user"""
        p = parcel_obj.get_theirs(user_id)
        if p == 404:
            return {"Error": "No deliveries by user"}, 404
        else:
            return {"Here are the deliveries by user": p}, 200


class Destination(Resource):
    """This class represents how the destination of a parcel may
    be manipulated"""

    def put(self, id):
        form = request.get_json()
        try:
            destination = form['destination']
        except KeyError:
            return {"Error": "Please enter a destination"}, 400
        res = parcel_obj.change_destination(id, destination)
        if res == 404:
            return {"Error": "Parcel not found"}, 404
        elif res == 201:
            return {"Success": "Destination Successfully changed"}, 201
        else:
            return {"Error": "Something went wrong"}, 400


class Admin(Resource):
    """This class represents the admin and the methods they can perfom"""

    def put(self, id):
        """This method should be used to change the destination
        of a delivery"""
        form = request.get_json()
        try:
            location = form['location']
        except KeyError:
            return {"Please enter location"}, 400
        parcel_obj.change_location(id, location)
        return {"Success": "Current location has been updated"}, 201


class Cancel(Resource):
    """This class is for cancelling a specific delivery order"""

    def put(self, id):
        """This method is for cancelling a specific delivery"""
        response = parcel_obj.cancel(id)
        if response == 200:
            return {"Success": "Delivery {} was cancelled".format(id)}
        elif response == 400:
            return {"Error": "Parcel has already been delivered."}
        else:
            return {"Error": "Parcel not found"}
