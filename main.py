from classes.shop import Shop
from classes.storage import Storage
from classes.store import Store
from classes.request import Request

if __name__ == "__main__":
    shop = Shop()
    shop.add("печеньки", 5)
    shop.add("конфетки", 5)
    shop.add("бананы", 5)
    shop.add("чай", 5)
    store = Store()
    store.add("бумага", 5)
