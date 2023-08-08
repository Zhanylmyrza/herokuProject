from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from courseApp.models import Category, Branch, Contact, Course
from courseApp.serializer import CategorySerializer, BranchSerializer, ContactSerializer, CourseSerializer

class CategoryViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category_data = {'name': 'Test Category', 'imgpath': 'test/path'}
        self.category = Category.objects.create(name='Test Category', imgpath='test/path')
        self.url = reverse('category-list')

    def test_list_categories(self):
        response = self.client.get(self.url)
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_category(self):
        response = self.client.post(self.url, self.category_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

    def test_retrieve_category(self):
        url = reverse('category-detail', args=[self.category.id])
        response = self.client.get(url)
        serializer = CategorySerializer(self.category)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_category(self):
        url = reverse('category-detail', args=[self.category.id])
        updated_data = {'name': 'Updated Category', 'imgpath': 'updated/path'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, 'Updated Category')
        self.assertEqual(self.category.imgpath, 'updated/path')

    def test_delete_category(self):
        url = reverse('category-detail', args=[self.category.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)

# Similar test classes can be added for other viewsets (BranchViewSet, ContactViewSet, CourseViewSet)
