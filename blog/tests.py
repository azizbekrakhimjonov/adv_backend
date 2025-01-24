from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Advertisement

class AdvertisementAPITestCase(APITestCase):

    def setUp(self):
        # Test uchun namuna ma'lumot yaratamiz
        self.advertisement = Advertisement.objects.create(
            title="Test Advertisement",
            description="Test description",
            video=SimpleUploadedFile("test_video.mp4", b"file_content", content_type="video/mp4"),
            is_active=True
        )
        self.list_url = reverse('advertisements-list')  # API uchun URL: /api/advertisements/

    def test_advertisement_list(self):
        """Reklama ro'yxatini olish testi"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), list)
        self.assertEqual(len(response.json()), Advertisement.objects.count())

    def test_advertisement_detail(self):
        """Reklama detallari testi"""
        detail_url = reverse('advertisements-detail', args=[self.advertisement.id])
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.advertisement.title)

    def test_create_advertisement(self):
        """Reklama yaratish testi"""
        video = SimpleUploadedFile("test_video.mp4", b"file_content", content_type="video/mp4")
        data = {
            "title": "New Advertisement",
            "description": "New description",
            "video": video,
            "is_active": True
        }
        response = self.client.post(self.list_url, data, format='multipart')  # format='multipart'
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Advertisement.objects.count(), 2)
        self.assertEqual(Advertisement.objects.last().title, "New Advertisement")

    def test_update_advertisement(self):
        """Reklamani yangilash testi"""
        detail_url = reverse('advertisements-detail', args=[self.advertisement.id])
        data = {
            "title": "Updated Advertisement",
            "description": "Updated description",
            "is_active": False
        }
        response = self.client.patch(detail_url, data, format='json')  # PATCH request va format='json'
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.advertisement.refresh_from_db()
        self.assertEqual(self.advertisement.title, "Updated Advertisement")
        self.assertFalse(self.advertisement.is_active)

    def test_delete_advertisement(self):
        """Reklamani o'chirish testi"""
        detail_url = reverse('advertisements-detail', args=[self.advertisement.id])
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Advertisement.objects.count(), 0)
