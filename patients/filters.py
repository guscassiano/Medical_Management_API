from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Consultation, Patient


class PatientFilterClass(AutoRQLFilterClass):
    MODEL = Patient


class ConsultationFilterClass(AutoRQLFilterClass):
    MODEL = Consultation
    FILTERS = [
        {
            'filter': 'patient_name',
            'source': 'patient_name__id',
        }
    ]
