from pages.base_page import BasePage
from pages.locators import YandexImagesLocators


class YandexImagesPage(BasePage):

    def __init__(self, driver):
        super(YandexImagesPage, self).__init__(driver)
        self.default_url = "https://yandex.ru/images/"

