from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsultationViewSet, PatientViewSet


router = DefaultRouter()
router.register('patient', PatientViewSet)
router.register('consultation', ConsultationViewSet)

urlpatterns = [
    path('', include(router.urls))
]