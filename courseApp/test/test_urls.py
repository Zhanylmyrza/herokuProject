from django.test import SimpleTestCase
from django.urls import reverse, resolve
from courseApp.views import CategoryViewSet, BranchViewSet, ContactViewSet, CourseViewSet

class TestUrls(SimpleTestCase): 
    def test_admin_url_is_resolved(self):
        url = reverse('admin:app_list', args=('courseApp',))
        print(resolve(url))

    def test_api_url_is_resolved(self):
        url = reverse('api-root')
        print(resolve(url))

    def test_category_url_is_resolved(self):
        url = reverse('category-list')
        print(resolve(url))

    def test_contact_url_is_resolved(self):
        url = reverse('contact-list')
        print(resolve(url))

    def test_course_url_is_resolved(self):
        url = reverse('course-list')
        print(resolve(url))

    def test_branch_url_is_resolved(self):
        url = reverse('branch-list')
        print(resolve(url))
