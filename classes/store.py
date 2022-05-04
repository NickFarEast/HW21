from .storage import Storage


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, name, count):
        is_found = False
        if self.get_free_space() >= count:
            for key in self.items.keys():
                if name == key:
                    self.items[key] = self.items[key] + count
                    is_found = True
            if not is_found:
                self.items[name] = count
            print("Товар добавлен")
        else:
            if self.get_free_space() != 0:
                print(f"Товар не может быть доставлен, т.к. место есть только на {self.get_free_space()} товаров")
            else:
                print(f"Товар не может быть доставлен, т.к. место закончилось")

    def remove(self, name, count):
        is_found = False
        for key in self.items.keys():
            if name == key:
                is_found = True
                if self.items[key] - count >= 0:
                    self.items[key] = self.items[key] - count
                else:
                    print(f"Слишком мало {name}")

        if not is_found:
            print(f"{name.title()} - нет на складе")

        if self.items[name] == 0 and is_found:
            del self.items[name]

    def get_item(self):
        return self.items

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_unique_item_count(self):
        return len(self.items.keys())

