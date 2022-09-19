from entity.courier import Courier
from entity.request import Request
from entity.shop import Shop
from entity.store import Store
from exeptions import InvalidRequest, BaseError

store = Store(items={
    "печенька": 27,
    "собачка": 25,
    "елка": 25
})

shop = Shop(items={
    "печенька": 5,
    "собачка": 2,
    "елка": 2
})

storeges = {
    "магазин": shop,
    "склад": store
}


def main():
    print("\nДобрый день\n")

    while True:
        for storage_name in storeges:
            print(f'Сейчас в {storage_name}:\n{storeges[storage_name].get_item()}')

        user_input = input(
            "Введите запрос в формате 'Доставить 3 печеньки из склад в магазин'\n"
            "Введите 'стоп' или 'stop' если хотите закончить\n"
        )
        if user_input in ('stop', 'стоп'):
            break

        try:
            request = Request(request=user_input, storages=storeges)
        except BaseError as e:
            print(e.massage)
            continue

        courier = Courier(
            request=request,
            storages=storeges
        )

        try:
            courier.move()
        except BaseError as e:
            print(e.massage)
            # courier.cancel()


if __name__ == "__main__":
    main()
