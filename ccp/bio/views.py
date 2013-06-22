from models import PersonalData

from django.shortcuts import render


def personal_data(request):
    pd = PersonalData.objects.get(id=1)
    return render(request, 'index.html', {'pd': pd})
