from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .banners import *


class BannerAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        create_banners()

        cls.urls = {
            'list': reverse('banners:banner_list')
        }

    def test_banner_list(self):
        response = self.client.get(self.urls['list'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Title 5')
        self.assertNotContains(response, 'Title 6')
