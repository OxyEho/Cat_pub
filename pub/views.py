import uuid

from django.shortcuts import render
from django.views import generic
from .models import BookedModel, TableModel
from .forms import BookingTableForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .entities.form_entity import FormEntity
from datetime import datetime, timezone


# Create your views here.


def index(request):
    return render(request, 'index.html')


def booking_table(request, pk):
    table = TableModel.objects.get(pk=pk)
    form = FormEntity(person_count=table.max_person_count, table_id=table.id)
    bookings = BookedModel.objects.filter(table_id=table.id).order_by('booked_date')
    if request.method == 'POST':
        if request.POST.get('booked_date') != '':
            form.booked_date = datetime.fromisoformat(request.POST.get('booked_date'))
        else:
            form.booked_date = None
        form.person_count = int(request.POST.get('person_count'))
        if form.is_valid():
            booked = BookedModel()
            booked.table_id = pk
            booked.booked_date = form.booked_date
            booked.person_count = form.person_count
            booked.booked_uid = uuid.uuid4()
            booked.save()
            return HttpResponseRedirect(f'{reverse("booked")}?id={booked.booked_uid}')
    return render(request, 'pub/tablemodel_detail.html', {'tablemodel': table, 'form': form, 'bookings': bookings})


def booked_view(request):
    booked_id = request.GET.get('id')
    try:
        booked = BookedModel.objects.get(booked_uid=booked_id)
    except Exception:
        booked = None
    return render(request, 'pub/booked.html', {'booked': booked})


def search_booking(request):
    if request.method == 'POST':
        booked_id = request.POST.get('booked_id')
        if booked_id:
            return HttpResponseRedirect(f'{reverse("booked")}?id={booked_id}')
    return HttpResponseRedirect(reverse('index'))


# class TableDetailView(generic.DetailView):
#     model = TableModel

    # def get_queryset(self):
    #     return ListAsQuerySet(list(tables.values()), model=TableModel)
