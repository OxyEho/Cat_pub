from .models import TableModel


class Table:
    def __init__(self, _id: int, max_person_count: int):
        self.id = _id
        self.max_person_count = max_person_count

    def get_model(self):
        table_model = TableModel
        table_model.id = self.id
        table_model.max_person_count = self.max_person_count


tables = {
    1: Table(1, 4).get_model(),
    2: Table(2, 4).get_model(),
    3: Table(3, 2).get_model(),
    4: Table(4, 2).get_model(),
    5: Table(5, 2).get_model(),
}
