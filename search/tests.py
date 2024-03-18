import json
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Group

from rest_framework_simplejwt.tokens import RefreshToken

import base64
from users.models import *

class SearchTestCase(TestCase):

	def setUp(self):
		# Set up data or create a test user if necessary
		Group.objects.create(name='admin')
		
		user = User.objects.create(email='test@test.com', username='test@test.com',first_name='test', 
									last_name="test", phone="5555555555", password="string123456", is_superuser=True)
		user.groups.add(1)
		refresh = RefreshToken.for_user(user)
		access = refresh.access_token
		print(access)

		self.token = base64.b64encode(str(access).encode()).decode()


	def test_search_api(self):
		data = {'query':'test'}
		response = self.client.post(reverse('search_view'),  data=json.dumps(data), HTTP_AUTHORIZATION=f'Octoxlabs {self.token}',content_type='application/json')

		print(response)
		self.assertEqual(response.status_code, 200)