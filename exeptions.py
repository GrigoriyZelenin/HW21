class BaseError(Exception):
    massage = "Неожиданная ошибка"


class NotEnoughSpace(BaseError):
    massage = 'Недостаточно места на складе'


class NotEnoughProduct(BaseError):
    massage = 'Недостаточно товара на складе'


class ToManyDifferentProducts(BaseError):
    massage = 'Слишком много разных товаров'


class InvalidRequest(BaseError):
    massage = 'Неправильный запрос, попробуйте снова'


class InvalidStorageName(BaseError):
    massage = 'Выбран несуществующий склад'
