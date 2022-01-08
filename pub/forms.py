from django import forms

from .models import TableModel, BookedModel

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime


class BookingTableForm(forms.ModelForm):
    class Meta:
        model = BookedModel
        fields = ['booked_date', 'person_count']
        labels = {
            'booked_date': _("Време бронирования столика"),
            'person_count': _("Количество человек")
        }

    def clean_booked_date(self):
        data = self.cleaned_data['booked_date']
        if data < datetime.datetime.now(datetime.timezone.utc):
            raise ValidationError(_('Нельзя бронировать столы в прошлом'),)
        return data
