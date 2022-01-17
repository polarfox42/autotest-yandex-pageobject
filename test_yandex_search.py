import pytest

from pages.yandex_images_pages import YandexImagesPage
from pages.yandex_search_pages import YandexSearchPage


REQUEST = "Тензор"
LINK = "tensor.ru"


def test_yandex_search(browser):
    page = YandexSearchPage(browser)
    page.go_to_site()
    page.can_see_search_field()
    page.enter_request(REQUEST)
    page.can_see_suggest()
    page.click_enter_on_search_field()
    page.can_see_search_results()
    page.got_link_in_top_5(LINK)


def test_yandex_images(browser):
    page = YandexImagesPage(browser)
    page.go_to_site()
    page.can_see_images_link()
    page.click_images_link()
    page.check_current_url()
    page.open_first_category()
    page.open_first_image()
    page.click_next()
    page.click_prev()
