# images/tests/test_api.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from images.models import Image
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from PIL import Image as PILImage

class ImageUploadTests(APITestCase):
    def setUp(self):
        # Подготовка тестового изображения
        self.image_path = os.path.join(os.path.dirname(__file__), 'test_image.jpg')
        image = PILImage.new('RGB', (100, 100), color = (73, 109, 137))
        image.save(self.image_path)

    def test_upload_image(self):
        url = reverse('image-upload')
        with open(self.image_path, 'rb') as image_file:
            data = {
                'original': SimpleUploadedFile(image_file.name, image_file.read(), content_type='image/jpeg'),
                'project_id': 111
            }
            response = self.client.post(url, data, format='multipart')
        print(response.content)  # Добавляем вывод содержимого ответа для отладки
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('original', response.data)
        self.assertIn('project_id', response.data)

    def test_get_images(self):
        # Создаем тестовое изображение
        Image.objects.create(original=SimpleUploadedFile(self.image_path, b'test content'), project_id=111)
        url = reverse('images-list', kwargs={'project_id': 111})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
