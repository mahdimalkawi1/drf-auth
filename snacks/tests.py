from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Snack
# Create your tests here.
class SnackTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()
        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass2"
        )
        testuser2.save() 

    

        test_snack = Snack.objects.create(
            title="rake",
            owner=testuser1,
            desc="Better for collecting leaves than a shovel.",
        )
        test_snack.save()

    def setUp(self) -> None:
         self.client.login(username="testuser1", password="pass")  

   
    def test_snacks_model(self):
        snack = Snack.objects.get(id=1)
        actual_owner = str(snack.owner)
        actual_name = str(snack.title)
        actual_desc = str(snack.desc)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_desc, "Better for collecting leaves than a shovel."
        )

    def test_get_snack_list(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snacks = response.data
        self.assertEqual(len(snacks), 1)
        self.assertEqual(snacks[0]["title"], "rake")


    def test_auth_required(self):
        self.client.logout() 
        url = reverse("snack_list")  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_only_owner_can_delete_snack(self):
        self.client.logout()
        self.client.login(username="testuser2", password="pass2")
        url = reverse("snack_detail",args=[1])  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_snack(self):
        self.client.logout()
        self.client.login(username="testuser1", password="pass")    
        url = reverse("snack_detail", args=[1])
        updated_data = {"title": "mansaf", "desc": "more delicious"}
        response = self.client.patch(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snack = Snack.objects.get(id=1)
        self.assertEqual(snack.title, updated_data["title"])
        self.assertEqual(snack.desc, updated_data["desc"])

    def test_only_owner_can_delete_snack2(self):
        self.client.logout()
        self.client.login(username="testuser1", password="pass")
        url = reverse("snack_detail",args=[1])  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    