from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from models import PersonalData, Request
from forms import PersonalDataForm


def personal_data(request):
    pd = PersonalData.objects.get(id=1)
    return render(request, 'index.html', {'pd': pd})


def stored_requests(request):
    latest = Request.objects.order_by('-date_added')[:10]
    return render(request, 'stored_requests.html', {'stored_requests': latest})


@login_required
def personal_data_update(request):
    form = PersonalDataForm(request.POST or None, files=request.FILES or None)
    is_saved = False
    if form.is_valid():
        form.save()
        is_saved = True
    photo = PersonalData.objects.get(id=1).photo
    return render(
        request, 'personal_data_update.html',
        {'form': form, 'is_saved': is_saved, 'photo': photo})
