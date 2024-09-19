from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Consultation, Patient


class ConsultationTest(APITestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            full_name="Roberta Maia",
            profession="Engenheiro",
            address="Rua Exemplo, 123",
            city="São Paulo",
            state="São Paulo",
            email="robmaia@outlook.com",
            phone="(11) 99999-9999",
            social_name="Robby"
        )
        self.consultation_data = {
            "consultation_data": "2024-09-20T14:15:00Z",
            "patient_name": self.patient.id,
        }
        self.consultation = Consultation.objects.create(
            consultation_data="2024-09-20T14:15:00Z",
            patient_name=self.patient
        )

    def test_create_consultation(self):
        url = reverse('consultation-list')
        response = self.client.post(url, self.consultation_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Consultation.objects.count(), 2)
        self.assertEqual(response.data['patient_name'], self.patient.id)

    def test_list_consultations(self):
        url = reverse('consultation-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_consultation(self):
        url = reverse('consultation-detail', kwargs={'pk': self.consultation.id})
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.consultation.id)

    def test_update_consultation(self):
        url = reverse('consultation-detail', kwargs={'pk': self.consultation.id})
        updated_data = {
            "consultation_data": "2024-10-02T10:30:00Z"
        }
        response = self.client.patch(url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.consultation.refresh_from_db()
        self.assertEqual(self.consultation.consultation_data.isoformat(), "2024-10-02T10:30:00+00:00")

    def test_delete_consultation(self):
        url = reverse('consultation-detail', kwargs={'pk': self.consultation.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Consultation.objects.count(), 0)