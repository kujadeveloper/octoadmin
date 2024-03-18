import json
from django.test import TestCase
from django.urls import reverse

class UserTestCase(TestCase):

    def test_user_api(self):
        print("*****Users TEST*****")
        data = {
		  "email": "string@string.com",
		  "username": "string",
		  "first_name": "string",
		  "last_name": "string",
		  "phone": "string",
		  "password": "string123",
		  "repassword": "string123"
		}
        
        response = self.client.post(reverse('users'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['success'])
        print("*****Users COMPLENT*****")
        
