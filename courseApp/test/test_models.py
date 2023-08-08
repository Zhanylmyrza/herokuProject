from django.test import TestCase
from courseApp.models import Category, Branch, Contact, Course

class CategoryModelTest(TestCase):
    def test_category_str_representation(self):
        category = Category(name="Test Category", imgpath="test/path")
        self.assertEqual(str(category), "Test Category")

class BranchModelTest(TestCase):
    def test_branch_str_representation(self):
        branch = Branch(latitude="40.7128", longitude="74.0060", address="Test Address")
        self.assertEqual(str(branch), "Test Address")

class ContactModelTest(TestCase):
    def test_contact_default_value(self):
        contact = Contact()
        self.assertEqual(contact.type, 1)

class CourseModelTest(TestCase):
    def test_course_str_representation(self):
        category = Category.objects.create(name="Test Category", imgpath="test/path")
        course = Course(name="Test Course", description="Test Description", category=category, logo="test/logo/path")
        self.assertEqual(str(course), "Test Course")

    def test_course_related_names(self):
        category = Category.objects.create(name="Test Category", imgpath="test/path")
        contact = Contact.objects.create()
        branch = Branch.objects.create(latitude="40.7128", longitude="74.0060", address="Test Address")

        course = Course.objects.create(name="Test Course", description="Test Description", category=category, logo="test/logo/path")
        course.contacts.add(contact)
        course.branches.add(branch)

        self.assertEqual(course.category.models.first(), course)
        self.assertEqual(course.contacts.first().models.first(), course)
        self.assertEqual(course.branches.first().models.first(), course)

