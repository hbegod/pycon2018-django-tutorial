from django.http import HttpResponse


DRAFT = 0
ACTIVE = 1
INCOMED = 2

INCOME_TYPES = {
    DRAFT: 'Черновик',
    ACTIVE: 'Активная',
    INCOMED: 'Завершенная',
}


def category(request, name_or_id):
    """Страница категории.

    :param request: HttpRequest
    :param name_or_id: Принимает либо slug либо id категории.
    :return:
    """
    return HttpResponse(
        f'<html><body>'
        f'<h1>Категория</h1>'
        f'<p>name_or_id: {name_or_id}</p>'
        f'</body></html>'
    )


def product(request, product_id):
    """Страница товара

    :param request: HttpRequest
    :param product_id: id товара.
    :return:
    """
    return HttpResponse(
        f'<html><body>'
        f'<h1>Товар</h1>'
        f'<p>product_id: {product_id}</p>'
        f'</body></html>'
    )


def incomes_list(request, income_type=None):
    """Список заявок c возможностью указния типа.
    Если типа нет, то будет сформирован в полный список.

    :param request: HttpRequest
    :param income_type: INCOME_TYPES.keys() or None
    :return:
    """
    return HttpResponse(
        f'<html><body>'
        f'<h1>Поступление</h1>'
        f'<p>income_type: {INCOME_TYPES[income_type]}</p>'
        f'</body></html>'
    )


def imcomes_for_date(request, admission_date, income_type=None):
    """Список заявок на дату, с возможностью указания типа.

    :param request: HttpRequest
    :param admission_date: Ожидаемая дата поступления.
    :param income_type: INCOME_TYPES.keys() or None
    :return:
    """
    return HttpResponse(
        f'<html><body>'
        f'<h1>Поступление</h1>'
        f'<p>admission_date: {admission_date}</p>'
        f'<p>income_type: {INCOME_TYPES[income_type]}</p>'
        f'</body></html>'
    )


def income_page(request, income_id):
    """Список заявок на дату, с возможностью указания типа.

    :param request: HttpRequest
    :param income_id: id поступления
    :return:
    """
    return HttpResponse(
        f'<html><body>'
        f'<h1>Поступление</h1>'
        f'<p>income_id: {income_id}</p>'
        f'</body></html>'
    )

