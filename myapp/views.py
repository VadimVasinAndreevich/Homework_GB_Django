import logging
import datetime
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def links(request):
    logger.info(f'Transition on links, {datetime.datetime.now()}')
    return HttpResponse(
        "<title>Ссылочная</title>"
        "<h3><a href='/index/'>.....Главная.....</a></h3>"
        "<h3><a href='/about/'>.....Информация.....</a></h3>"
    )


def index(request):
    logger.info(f'Transition on main page, {datetime.datetime.now()}')
    return HttpResponse(
        "<title>Главная</title>"
        "<h2>Это главная страница сайта</h2>"
        "<p>На этой странице основная информация сайта"
        "<h3><a href='/about/'>.....Информация.....</a></h3>"
        )


def about(request):
    logger.info(f'Transition on page with information, {datetime.datetime.now()}')
    return HttpResponse(
        "<title>Информация</title>"
        "<h2>Это страница с информацией сайта</h2>"
        "<p>Привет, это первая тестовая страница сайта на Django, я только начал изучать данный фреймворк, "
        "поэтому страница выглядит мягко говоря не очень, и этот текст предан не через  текстовый файл html</p>"
        "<br>"
        "<p>Очень понравились лекции и семинары по Flask и FastAPI, надеюсь скоро также изучить и Django"
        "<h3><a href='/index/'>.....Главная.....</a></h3>"
        )
