from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Build Courses API",
      default_version='v1',
      description="I just implemented a simple REST API for building courses using Django and Django Rest Framework with PostgreSQL database .",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="bkrvj83@gmail.com"),
      license=openapi.License(name="B.Zh License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('', include("courseApp.urls"))
   
]  