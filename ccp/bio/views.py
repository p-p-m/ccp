from models import PersonalData, Request

from django.shortcuts import render


def personal_data(request):
    pd = PersonalData.objects.get(id=1)
    return render(request, 'index.html', {'pd': pd})


def stored_requests(request):
    latest = Request.objects.order_by('-date_added').all()
    return render(request, 'stored_requests.html', {'stored_requests': latest})
