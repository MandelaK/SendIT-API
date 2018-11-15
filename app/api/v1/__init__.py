from .views import (GenericParcel, User, SpecificParcel,
                    Admin, Cancel, Destination)
from flask import Blueprint
from flask_restful import Api

version1 = Blueprint("v1", __name__, url_prefix="/api/v1")
api = Api(version1, catch_all_404s=True)

api.add_resource(GenericParcel, "/parcels")
api.add_resource(User, "/users/<int:user_id>/parcels")
api.add_resource(SpecificParcel, "/parcels/<int:parcel_id>")
api.add_resource(Admin, "/admin/location/<int:parcel_id>")
api.add_resource(Cancel, "/parcels/<int:parcel_id>/cancel")
api.add_resource(Destination, "/parcels/<int:parcel_id>/destination")
