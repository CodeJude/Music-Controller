from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Room


class RoomViewTestCase(APITestCase):

    def setUp(self):
        # Create some sample rooms for testing
        self.room1 = Room.objects.create(
            code="ABC123", host="Host1", guest_can_pause=True, vote_to_skip=3)
        self.room2 = Room.objects.create(
            code="DEF456", host="Host2", guest_can_pause=False, vote_to_skip=2)

    def test_list_rooms(self):
        # Assuming you named the view 'RoomView' as 'room-list'
        response = self.client.get(reverse('room-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assuming there are two rooms in the database
        self.assertEqual(len(response.data), 2)

    def test_api_listview(self):
        response = self.client.get(reverse('room-list'))
        # Check that the response data matches the data of the created rooms
        self.assertEqual(response.data[0]['code'], self.room1.code)
        self.assertEqual(response.data[0]['host'], self.room1.host)
        self.assertEqual(
            response.data[0]['guest_can_pause'], self.room1.guest_can_pause)
        self.assertEqual(
            response.data[0]['vote_to_skip'], self.room1.vote_to_skip)

    def test_api_secondView(self):
        response = self.client.get(reverse('room-list'))
        self.assertEqual(response.data[1]['code'], self.room2.code)
        self.assertEqual(response.data[1]['host'], self.room2.host)
        self.assertEqual(
            response.data[1]['guest_can_pause'], self.room2.guest_can_pause)
        self.assertEqual(
            response.data[1]['vote_to_skip'], self.room2.vote_to_skip)

    # Add more test cases for other API views, if you have any
