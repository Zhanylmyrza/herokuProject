from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from courseApp.models import Category, Branch, Contact, Course
from courseApp.serializer import CategorySerializer, BranchSerializer, ContactSerializer, CourseSerializer


class CategoryViewSet(viewsets.ModelViewSet):
  
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
 

class BranchViewSet(viewsets.ModelViewSet):
  
  queryset = Branch.objects.all()
  serializer_class = BranchSerializer
  
class ContactViewSet(viewsets.ModelViewSet):
  
  queryset = Contact.objects.all()
  serializer_class = ContactSerializer
  

class CourseViewSet(viewsets.ModelViewSet):
  
  queryset = Course.objects.all()
  serializer_class = CourseSerializer
 