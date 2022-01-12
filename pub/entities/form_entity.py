import datetime

from ..models import BookedModel, TableModel


class FormEntity:
    def __init__(self, person_count: int, table_id: int, booked_date: datetime.datetime = datetime.datetime.now()):
        self.booked_date = booked_date
        self.person_count = person_count
        self.table_id = table_id
        self.err = ErrMsg()

    def is_valid(self):
        table = TableModel.objects.get(id=self.table_id)
        if not self.booked_date:
            self.err.empty_date = True
            return False
        if self.booked_date < datetime.datetime.now():
            self.err.past = True
            return False
        query_set = BookedModel.objects.filter(table_id=self.table_id,
                                               booked_date__lt=self.booked_date + datetime.timedelta(hours=1),
                                               booked_date__gt=self.booked_date - datetime.timedelta(hours=1))
        if query_set:
            self.err.booked = True
            return False
        if table.max_person_count < self.person_count:
            self.err.to_many = True
            return False
        if self.person_count <= 0:
            self.err.negative = True
            return False
        return True


class ErrMsg:
    msg_empty_date = 'Время не может быть пустым'
    msg_past = 'Нельзя бронировать в прошлом'
    msg_booked = 'Это время занято'
    msg_to_many = 'Слишком много людей'
    msg_negative = 'Не положиельное число людей'

    def __init__(self):
        self.past = False
        self.booked = False
        self.to_many = False
        self.negative = False
        self.empty_date = False
