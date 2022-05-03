from abc import abstractmethod


class Storage:
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_item(self):
        pass

    @abstractmethod
    def get_unique_item_count(self):
        pass
