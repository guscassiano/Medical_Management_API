from rest_framework import viewsets, permissions
from .serializers import PatientSerializer, ConsultationSerializer
from .models import Patient, Consultation
from dj_rql.drf import RQLFilterBackend
from .filters import PatientFilterClass, ConsultationFilterClass


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = PatientFilterClass
    permission_classes = [permissions.DjangoModelPermissions]


class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = ConsultationFilterClass
    permission_classes = [permissions.DjangoModelPermissions]