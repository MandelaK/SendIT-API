from flask_restful import Resource
from flask_restful.reqparse import RequestParser as R
from .models import Parcel
from flask import request

parcel_obj = Parcel()


class GenericParcel(Resource):
    """This class contains generic parcels without
    any specificity."""

    def __init__(self):
        self.inspect = R()
        self.inspect.add_argument(
            "sender", help="Please enter a sender name", required=True)
        self.inspect.add_argument(
            "parcel_name", help="Please enter a parcel name", required=True)
        self.inspect.add_argument(
            "recipient", help="Please enter a recipient", required=True)
        self.inspect.add_argument(
            "user_id", help="Please enter a user id", required=True)
        self.inspect.add_argument(
            "weight", help="Please enter the weight", required=True)
        self.inspect.add_argument(
            "pickup", help="Please enter the pickup location", required=True)
        self.inspect.add_argument(
            "destination", help="Please enter destination", required=True)

    def get(self):
        parcels = parcel_obj.get_all()
        return parcels

    def post(self):
        """This method is for adding a delivery to our database."""
        parcel_data = self.inspect.parse_args()

        response = parcel_obj.add_parcel(parcel_data['sender'],
                                         parcel_data['parcel_name'],
                                         parcel_data['user_id'],
                                         parcel_data['recipient'],
                                         parcel_data['destination'],
                                         parcel_data['weight'],
                                         parcel_data['pickup'])
        if response == 201:
            return {"Success": "Successfully added your delivery"}, 201


class SpecificParcel(Resource):
    """This class contains methods for manipulating a specific parcel"""

    def get(self, parcel_id):
        """This method should return a parcel if we are sent it's id"""
        response = parcel_obj.get_parcel(parcel_id)
        if response == 404:
            return {"Error": "Parcel does not exist"}, 404
        return response


class User(Resource):
    """This class represents the user and what actions they can do to their
    parcels"""

    def get(self, user_id):
        """This method gets all deliveries sent by a user"""
        items = parcel_obj.get_theirs(user_id)
        if items == 404:
            return {"Error": "No deliveries by user"}, 404
        else:
            return items


def valid_location(location):
    """This function verifies that location entered is valid"""
    if type(location) == int:
        return False
    elif bool(location.strip()) is False:
        return False
    elif location.isalpha() is False:
        return False
    else:
        return True


class Destination(Resource):
    """This class represents how the destination of a parcel may
    be manipulated"""

    def put(self, parcel_id):
        form = request.get_json()
        try:
            destination = form['destination']
        except KeyError:
            return {"Error": "Please enter a destination"}, 400
        verify_location = valid_location(destination)
        if not verify_location:
            return {"Error": "Please enter a valid destination"}, 400
        else:
            res = parcel_obj.change_destination(parcel_id, destination)
        if res == 404:
            return {"Error": "Parcel not found"}, 404
        elif res == 201:
            return {"Success": "Destination Successfully changed"}, 201
        else:
            return {"Error": "Parcel already delivered"}, 400


class Admin(Resource):
    """This class represents the admin and the methods they can perfom"""

    def put(self, parcel_id):
        """This method should be used to change the destination
        of a delivery"""
        form = request.get_json()
        try:
            location = form['location']
        except KeyError:
            return {"Error": "Please enter location"}, 400
        verify_location = valid_location(location)
        if not verify_location:
            return {"Error": "Please enter a valid location"}
        else:
            res = parcel_obj.change_location(parcel_id, location)

        if res == 201:
            return {"Success": "Current location has been updated"}, 201
        else:
            return 404


class Cancel(Resource):
    """This class is for cancelling a specific delivery order"""

    def put(self, parcel_id):
        """This method is for cancelling a specific delivery"""
        response = parcel_obj.cancel(parcel_id)
        if response == 200:
            return {"Success": "Delivery {} was cancelled".format(parcel_id)}
        elif response == 400:
            return {"Error": "Parcel has already been delivered."}
        else:
            return {"Error": "Parcel not found"}
