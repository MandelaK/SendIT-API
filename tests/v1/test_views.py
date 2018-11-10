import unittest
import json

from run import app


parcel = {
    'id': 1,
    'sender': 'Mandela',
    'user_id': 100,
    'recipient': 'Jane',
    'destination': 'Heaven',
    'weight': '69',
    'pickup': 'Hell',
    'location': 'Hell',
    'status': 'pending'
}


class ParcelTestCase(unittest.TestCase):

    def setUp(self):
        """This should be called before each test"""
        self.app = app
        self.client = app.test_client(self)
        self.app.testing = True
        self.parcel = parcel
        self.app_context = self.app.app_context()
        self.app_context.push()


class TestValidRequest(ParcelTestCase):
    """This is the testcase for when the user submits valid data"""

    def test_we_successfully_create_order(self):
        """This will test POST /parcels"""
        res = self.client.post(
            'api/v1/parcels', data=json.dumps(self.parcel), content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_we_get_all_parcels(self):
        """Test GET /parcels to see if we can get all orders"""
        res = self.client.get('/api/v1/parcels', data=json.dumps(self.parcel),
                              content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_we_can_cancel_parcel(self):
        """Test PUT /parcels/id/cancel to see if we can cancel specific
        parcel"""
        res = self.client.put('/api/v1/parcels/1/cancel',
                              data=json.dumps(self.parcel),
                              content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_we_get_specific_parcel_we_requested(self):
        res = self.client.get('/api/v1/parcels/1', data=json.dumps(self.parcel),
                              content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_we_can_get_parcels_by_one_user(self):
        res = self.client.get('/api/v1/users/100/parcels', data=json.dumps(self.parcel),
                              content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_we_successfully_change_location(self):
        res = self.client.put('/api/v1/admin/location/1', data=json.dumps(self.parcel),
                              content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_we_can_change_destination(self):
        res = self.client.put('/api/v1/parcels/1/destination',
                              data=json.dumps(self.parcel),
                              content_type='application/json')
        self.assertEqual(res.status_code, 201)

    # def test_we_return_parcel_with_correct_id(self):
    #     pass

    # def test_we_return_error_if_user_sends_string_as_id(self):
    #     pass

    # def test_we_return_404_if_parcel_id_does_not_exist(self):
    #     pass

    # # we test our SpecificParcel.post() method
    # def test_we_return_bad_request_if_user_doesnt_send_request_in_json(self):
    #     pass

    # def test_we_return_bad_request_if_user_is_missing_sender_key(self):
    #     pass

    # def test_we_return_bad_request_if_user_is_missing_destination_key(self):
    #     pass

    # def test_we_return_bad_request_if_user_is_missing_pickup_key(self):
    #     pass

    # def test_we_return_bad_request_if_user_is_missing_recipient_key(self):
    #     pass

    # def test_we_return_bad_request_if_user_is_missing_weight_key(self):
    #     pass

    # def test_we_return_201_on_successful_creation_of_submitted_delivery(self):
    #     pass

    # def test_return_error_if_user_not_logged_in_try_to_create_delivery(self):
    #     pass

    # def test_test_if_id_is_added_to_all_appended_requests(self):
    #     pass

    # # we test our SpecificParcel.put(id) method
    # def test_return_bad_request_if_user_is_missing_new_destination_key(self):
    #     pass

    # def test_we_return_bad_request_if_user_is_missing_id(self):
    #     pass

    # def test_we_return_error_if_user_does_not_have_authentication(self):
    #     pass

    # def test_we_return_bad_request_if_request_not_sent_in_json(self):
    #     pass

    # def test_we_return_bad_request_if_id_not_found_in_request(self):
    #     pass

    # def test_we_return_forbidden_if_delivery_status_not_in_transit(self):
    #     pass

    # def test_we_append_modified_delivery_in_our_database(self):
    #     pass

    # def test_we_return_modified_delivery_to_user_with_relevant_code(self):
    #     pass

    # def test_ensure_destination_key_is_string(self):
    #     pass

    # # we test the SpecificParcel.delete(id)
    # def test_we_return_bad_request_if_no_id_is_provided(self):
    #     pass

    # def test_we_return_error_if_user_not_authorized(self):
    #     pass

    # def test_we_delete_the_delivery_sent_by_user(self):
    #     pass
