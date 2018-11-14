# This is our models file where we store our temporary storage data and methods
# to manipulate the data. Our parcels list is globally available all classes
# that inherit the Parcel class

# this is where all our parcels will be appended
parcels = [
    {
        "parcel_id": 1,
        "parcel_name": "Success cards",
        "sender": "Keith",
        "user_id": 100,
        "recipient": "Juma",
        "destination": "Nairobi",
        "weight": "500",
        "pickup": "Ruiru",
        "location": "Ruiru",
        "status": "pending"
    }, {
        "parcel_id": 2,
        "parcel_name": "Divorce Letter",
        "sender": "John",
        "user_id": 101,
        "recipient": "Steve",
        "destination": "Kiambu",
        "weight": "920",
        "pickup": "Naivasha",
        "location": "Naivasha",
        "status": "pending"
    }, {
        "parcel_id": 3,
        "parcel_name": "Job contract",
        "sender": "Keith",
        "user_id": 100,
        "recipient": "Peter",
        "destination": "Vihiga",
        "weight": "900",
        "pickup": "Kericho",
        "location": "Vihiga",
        "status": "delivered"
    }
]


class Parcel(object):
    """This is the parcel class"""

    def __init__(self):
        self.db = parcels
        self.status = "pending"

    def return_valid_parcel(self, parcel_id):
        p = [parcel for parcel in self.db if parcel["parcel_id"] == parcel_id]
        if p:
            return p[0]
        return False

    def add_parcel(self, sender, parcel_name, user_id, recipient, destination,
                   weight, pickup):
        """The method to create a delivery and append
            it to our list"""

        # we check the request object the user sends to
        # validate it has enough information then add to payload

        data = {
            "parcel_id": len(parcels) + 1,
            "sender": sender,
            "parcel_name": parcel_name,
            "user_id": user_id,
            "recipient": recipient,
            "destination": destination,
            "weight": weight,
            "pickup": pickup,
            "location": pickup,
            "status": self.status
        }

        self.db.append(data)
        return 201

    def get_all(self):
        """Defines the method to get all parcel deliveries GET /parcels"""
        return self.db, 200

    def get_parcel(self, parcel_id):
        """Defines method to get a specific delivery with it"s key
         GET /parcels/<int:id>"""
        item = self.return_valid_parcel(parcel_id)
        if not item:
            return 404
        return item, 200

    def cancel(self, parcel_id):
        """Defines the method for deleting a specific delivery from the
        database"""
        item = self.return_valid_parcel(parcel_id)
        if not item:
            return 404
        elif item["status"] is not "delivered":
            item.update({"status": "cancelled"})
            return 200
        else:
            return 400

    def get_theirs(self, user_id):
        """"Defines the method for getting all deliveries from a specific
        sender"""
        orders = []
        for parcel in self.db:
            if parcel["user_id"] == user_id:
                orders.append(parcel)
        if orders == []:
            return 404
        return orders

    def change_location(self, parcel_id, location):
        """Defines the method for changing the
        current location of a delivery"""
        item = self.return_valid_parcel(parcel_id)
        if not item:
            return 404
        else:
            item.update({"location": location})
            return 201

    def change_destination(self, parcel_id, destination):
        """We use this method to change the destination of the
        requested delivery"""
        item = self.return_valid_parcel(parcel_id)
        if not destination:
            return {"Error": "Please add a destination"}
        elif not item:
            return 404
        elif item["status"] is not "delivered":
            item.update({"destination": destination})
            return 201
        else:
            return 400
