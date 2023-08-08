from django.urls import include,path
from django.contrib import admin
from django.urls import include,path
from rest_framework.routers import DefaultRouter
from courseApp import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router=DefaultRouter()
router.register(r"category", views.CategoryViewSet)
router.register(r"contact", views.ContactViewSet)
router.register(r"course", views.CourseViewSet)
router.register(r"branch", views.BranchViewSet)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/', include(router.urls)),
  
]



