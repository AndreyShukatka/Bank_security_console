import os
import django
from django.shortcuts import render
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()
from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import get_duration
from datacenter.models import is_visit_long
from datacenter.models import format_duration
from django.shortcuts import get_object_or_404, get_list_or_404


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = get_object_or_404(Passcard, passcode=passcode)
    all_visits = get_list_or_404(Visit, passcard=passcard)
    is_strange = False
    for visit in all_visits:
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': format_duration(get_duration(visit)),
                'is_strange': is_visit_long(visit, minutes=60)
            }

        )


        context = {
            'passcard': passcard,
            'this_passcard_visits': this_passcard_visits
        }
    return render(request, 'passcard_info.html', context)
