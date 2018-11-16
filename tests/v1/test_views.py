import unittest
import json

from run import app


parcel = {
    "parcel_id": 1,
    "sender": "Mandela",
    "parcel_name": "Trial",
    "user_id": 100,
    "recipient": "Jane",
    "destination": "Heaven",
    "weight": "69",
    "pickup": "Hell",
    "location": "Hell",
    "status": "transit"
}

no_sender_name = {
    "parcel_id": 2,
    "sender": "",
    "parcel_name": "Trial",
    "user_id": 100,
    "recipient": "Jane",
    "destination": "Heaven",
    "weight": "69",
    "pickup": "Hell",
    "location": "Hell",

}

no_parcel_name = {
    "parcel_id": 1,
    "sender": "Mandela",
    "parcel_name": "",
    "user_id": 100,
    "recipient": "Jane",
    "destination": "Heaven",
    "weight": "69",
    "price": "207",
    "pickup": "Hell",
    "location": "Hell",
}

no_weight = {
    "parcel_id": 1,
    "sender": "Mandela",
    "parcel_name": "Trial",
    "user_id": 100,
    "recipient": "Jane",
    "destination": "Heaven",
    "weight": "",
    "price": "",
    "pickup": "Hell",
    "location": "Hell",
}

no_destination = {
    "parcel_id": 1,
    "sender": "Mandela",
    "parcel_name": "Trial",
    "user_id": 100,
    "recipient": "Jane",
    "destination": "",
    "weight": "69",
    "pickup": "Hell",
    "location": "Hell",
}

fake_location = {
    "parcel_id": 1,
    "sender": "Mandela",
    "parcel_name": "Trial",
    "user_id": 100,
    "recipient": "Jane",
    "destination": "",
    "weight": "69",
    "pickup": "Hell",
    "location": "2342342",
}

no_sender = {
    "parcel_id": 1,
    "parcel_name": "Trial",
    "user_id": 100,
    "recipient": "Jane",
    "destination": "",
    "weight": "69",
    "pickup": "Hell",
    "location": "2342342"
}

weight_is_zero = {
    "parcel_id": 1,
    "parcel_name": "Trial",
    "user_id": 100,
    "recipient": "Jane",
    "destination": "Hell",
    "weight": "0",
    "price": "23",
    "pickup": "Hell",
    "location": "2342342"
}


class ParcelTestCase(unittest.TestCase):

    def setUp(self):
        """This should be called before each test"""
        self.app = app
        self.client = app.test_client(self)
        self.app.testing = True
        self.parcel = parcel


class TestValidRequest(ParcelTestCase):
    """This is the testcase for when the user submits valid data"""

    def test_we_successfully_create_order(self):
        """This will test POST /parcels"""
        res = self.client.post(
            "api/v1/parcels", data=json.dumps(self.parcel), content_type="application/json")
        self.assertEqual(res.status_code, 201)

    def test_we_get_all_parcels(self):
        """Test GET /parcels to see if we can get all orders"""
        res = self.client.get("/api/v1/parcels")
        self.assertEqual(res.status_code, 200)

    def test_we_can_cancel_parcel(self):
        """Test PUT /parcels/id/cancel to see if we can cancel specific
        parcel"""
        res = self.client.put("/api/v1/parcels/1/cancel")
        self.assertEqual(res.status_code, 201)

    def test_we_get_specific_parcel_we_requested(self):
        res = self.client.get("/api/v1/parcels/1")
        self.assertEqual(res.status_code, 200)

    def test_we_can_get_parcels_by_one_user(self):
        res = self.client.get("/api/v1/users/100/parcels")
        self.assertEqual(res.status_code, 200)

    def test_we_successfully_change_location(self):
        res = self.client.put("/api/v1/admin/location/1", data=json.dumps(self.parcel),
                              content_type="application/json")
        print(self.parcel)
        print(res)
        self.assertEqual(res.status_code, 201)

    def test_we_can_change_destination(self):
        res = self.client.put("/api/v1/parcels/1/destination",
                              data=json.dumps(self.parcel),
                              content_type="application/json")
        self.assertEqual(res.status_code, 201)


class TestInvalidRequest(ParcelTestCase):
    """From this class, we will test what happens when the user enters invalid input"""

    def test_user_cannot_get_parcel_that_does_not_exist(self):
        res = self.client.get("/api/v1/parcels/10")
        self.assertEqual(res.status_code, 404)

    def test_user_can_change_destination_of_parcels_that_only_exist(self):
        res = self.client.put("/api/v1/parcels/10/destination",
                              data=json.dumps(self.parcel), content_type="application/json")
        self.assertEqual(res.status_code, 404)

    def test_user_must_add_destination_when_making_order(self):
        res = self.client.post(
            "/api/v1/parcels", data=json.dumps(no_destination), content_type="application/json")
        self.assertEqual(res.status_code, 400)

    def test_user_must_include_weight_when_making_order(self):
        res = self.client.post(
            "/api/v1/parcels", data=json.dumps(no_weight), content_type="application/json")
        self.assertEqual(res.status_code, 400)

    def test_user_must_enter_parcel_name(self):
        res = self.client.post(
            "/api/v1/parcels", data=json.dumps(no_parcel_name), content_type="application/json")
        self.assertEqual(res.status_code, 400)

    def test_user_must_add_sender_name(self):
        res = self.client.post(
            "/api/v1/parcels", data=json.dumps(no_sender_name), content_type="application/json")
        self.assertEqual(res.status_code, 400)

    def test_user_enters_numbers_in_location(self):
        res = self.client.post(
            "/api/v1/parcels", data=json.dumps(fake_location), content_type="application/json")
        self.assertEqual(res.status_code, 400)

    def test_user_does_not_include_sender_at_all(self):
        res = self.client.post(
            "/api/v1/parcels", data=json.dumps(no_sender), content_type="application/json")
        self.assertEqual(res.status_code, 400)

    def test_weight_cannot_be_zero(self):
        res = self.client.post(
            "/api/v1/parcels", data=json.dumps(weight_is_zero), content_type="application/json")
        self.assertEqual(res.status_code, 400)
