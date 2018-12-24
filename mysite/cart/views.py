from django.http import HttpResponse


def cart(request):
    """Корзина.

    :param request: HttpRequest
    :return:
    """
    return HttpResponse('<html><body><h1>Корзина</h1></body></html>')


def shipping_form(request):
    """Достака

    :param request: HttpRequest
    :return:
    """
    return HttpResponse('<html><body><h1>Доставка</h1></body></html>')


def payment_form(request):
    """Оплата

    :param request: HttpRequest
    :return:
    """
    return HttpResponse('<html><body><h1>Оплата</h1></body></html>')


def success(request):
    """Оплата подтверждена.

    :param request: HttpRequest
    :return:
    """
    return HttpResponse('<html><body><h1>Успех</h1></body></html>')


def failure(request):
    """Отказ к оплате.

    :param request: HttpRequest
    :return:
    """
    return HttpResponse('<html><body><h1>Отказ</h1></body></html>')

