from django.http import HttpResponse
from django.shortcuts import render


def sales(request):
    """История покупок пользователя.

    :param request: HttpRequest
    :return:
    """
    return HttpResponse('<html><body><h1>История покупок.</h1></body></html>')


def favorite(request):
    """Избраное пользователя.

    :param request: HttpRequest
    :return:
    """
    return HttpResponse('<html><body><h1>Избраное</h1></body></html>')


def category_analytic(request, category=None, user_email=None):
    """Сводная таблица по категориям и пользователям.

    :param request: HttpRequest
    :param category: slug or None
    :param user_email: email or None
    :return:
    """
    return HttpResponse(
        f'<html><body>'
        f'<h1>Отчет</h1>'
        f'<p>category: {category}</p>'
        f'<p>user_email: {user_email}</p>'
        f'</body></html>'
    )
