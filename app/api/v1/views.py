from flask_restful import Resource
from .models import Parcel
from flask import request

parcel_obj = Parcel()


class GenericParcel(Resource):
    """This class contains generic parcels without
    any specificity."""

    def get(self):
        """This will be called when the user wants to get all delivery orders"""
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
            return {"Success": "Successfully added delivery"}, 201
