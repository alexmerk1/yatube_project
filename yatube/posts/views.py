from django.http import HttpResponse


def index(request):
    # Функция главной страницы
    return HttpResponse('Главная страница, т.е. Самая самая главная :-)')


def posts_group(request, slug):
    # Функция страницы поста
    return HttpResponse(f'На этой странице информация поста номер: {slug}')
