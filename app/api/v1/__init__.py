from flask import Blueprint
from flask_restful import Api

from .views import GenericParcel, SpecificParcel, Cancel, Admin, Destination

version1 = Blueprint('v1', __name__, url_prefix='/api/v1')
api = Api(version1)

api.add_resource(GenericParcel, '/parcels')
api.add_resource(SpecificParcel, '/parcels/<int:id>')
api.add_resource(Admin, '/admin/location/<int:id>')
api.add_resource(Cancel, '/parcels/<int:id>/cancel')
api.add_resource(Destination, '/parcels/<int:id>/destination')
