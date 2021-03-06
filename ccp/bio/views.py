from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from models import PersonalData, Request
from forms import PersonalDataForm, SortForm


def personal_data(request):
    pd = PersonalData.objects.get(id=1)
    return render(request, 'index.html', {'pd': pd})


def stored_requests(request):
    form = SortForm(request.GET or None)
    order = form.order_by() if form.is_valid() else 'date_added'
    latest = Request.objects.order_by(order)[:10]
    return render(request, 'stored_requests.html', {'stored_requests': latest, 'form': form})


@login_required
def personal_data_update(request):
    form = PersonalDataForm(request.POST or None, files=request.FILES or None)
    is_saved = False
    if request.is_ajax():
        if form.is_valid():
            is_saved = True
            form.save()
        photo = PersonalData.objects.get(id=1).photo
        return render(
            request, 'form.html', {'form': form, 'is_saved': is_saved, 'photo': photo})
    photo = PersonalData.objects.get(id=1).photo
    return render(
        request, 'personal_data_update.html',
        {'form': form, 'photo': photo})
