import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit, is_visit_long

if __name__ == '__main__':
    active_visits = Visit.objects.filter(leaved_at=None)
    suspicious_visits1 =[]
    passcards = Passcard.objects.all()
    for passcard in passcards:
        for visit in Visit.objects.filter(passcard=passcard):
            if is_visit_long(visit, minutes=60) == True:
                suspicious_visits1.append(visit)
    print(suspicious_visits1)
