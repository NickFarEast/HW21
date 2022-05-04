from .store import Store


class Shop(Store):
    def __init__(self, limit=5):
        super().__init__()
        self.items = {}
        self.capacity = 30
        self._limit = limit

    @property
    def get_item_limit(self):
        return self._limit

    def add(self, name, count):
        if self.get_unique_item_count() <= self._limit:
            super().add(name, count)
        else:
            print("Товар не может быть добавлен")



