from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .categories import *


class CategoriesAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        create_categories()
        cls.urls = {
            'test_category_list': reverse('tests:test_category_list'),
            'subject_list': reverse('tests:subject_list'),
            'topic_list': reverse('tests:topic_list')
        }

    def test_test_category_list(self):
        response = self.client.get(path=self.urls['test_category_list'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Description 1')

    def test_subject_list(self):
        response = self.client.get(path=self.urls['subject_list'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Title 1')

    def test_topic_list(self):
        response = self.client.get(path=self.urls['topic_list'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Title 1')
        self.assertContains(response, 'Title 3')
        self.assertContains(response, 'Title 5')

    def test_topic_list_filters(self):
        response = self.client.get(path=self.urls['topic_list'] + '?subject=2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Title 3')
        self.assertContains(response, 'Title 4')
        self.assertNotContains(response, 'Title 1')
        self.assertNotContains(response, 'Title 2')
        self.assertNotContains(response, 'Title 5')
        self.assertNotContains(response, 'Title 6')
