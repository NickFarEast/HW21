from classes.shop import Shop
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

    user_str = input()
    user_str_list = user_str.split(" ")
    is_error = False
    try:
        user_str_list[1] = int(user_str_list[1])
    except:
        print("Введите  число")
        is_error = True

    if ("забрать" and "доставить") not in user_str_list[0].lower():
        print("Введите забрать/доставить")
        is_error = True

    if ("магазин" and "склад") not in user_str_list[4].lower():
        print("Введите место назначения")
        is_error = True

    if not is_error:
        r = Request(user_str)
        print(r)
        if "магазин" in r.from_:
            print("Доставка возможна только со склада")
        elif "склад" in r.from_:
            if r.product in store.get_item():
                if r.amount <= store.get_item()[r.product]:
                    print("Нужное количество есть на складе")
                    print("Курьер везет со склада в магазин")
                    if sum(shop.get_item().values()) + int(r.amount) <= shop.capacity:
                        print(f"Курьер доставил {r.amount} {r.product} в магазин")
                        store.remove(r.product, r.amount)
                        shop.add(r.product, r.amount)
                    else:
                        print("В магазине недостаточно места, попробуйте заказать что-то другое")
                else:
                    print("Не хватает на складе , попробуйте заказать меньше")
            else:
                print("Такого товара нет на складе")

        if shop.get_unique_item_count():
            print("В магазине хранится:")
            for key, value in shop.items.items():
                print(key, value)
        else:
            print("В магазине пусто")

        if store.get_unique_item_count():
            print("На складе хранится:")
            for key, value in store.items.items():
                print(key, value)
        else:
            print("На складе пусто")
