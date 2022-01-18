from pages.base_page import BasePage
from pages.locators import YandexImagesLocators
import json
import urllib


class YandexImagesPage(BasePage):

    def __init__(self, driver):
        super(YandexImagesPage, self).__init__(driver)
        self.default_url = "https://yandex.ru/images/?utm_source=main_stripe_big"
        self.first_image = None

    def can_see_images_link(self):
        assert self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGES_PAGE_LINK), \
            "There's no link to Yandex.Images on the page"

    def click_images_link(self):
        link = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGES_PAGE_LINK)
        link.click()
        self.wait_for_new_window(2)

    def check_current_url(self):
        current_window = self.driver.current_window_handle
        for window in self.driver.window_handles:
            if window != current_window:
                self.driver.switch_to.window(window)
                break
        assert self.driver.current_url == self.default_url, f"Wrong url. Expected {self.default_url}, " \
                                                            f"got {self.driver.current_url}"

    def open_first_category(self):
        category = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGES_FIRST_POPULAR_REQUEST_ITEM)
        category_text = category.text
        category.click()
        search_text = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGES_SEARCH_FIELD).get_attribute('value')
        assert category_text == search_text, f"Wrong request text. Expected {category_text}, got {search_text}"

    def open_first_image(self):
        image = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGES_FIRST_FOUND_ITEM)
        data = json.loads(self.find_element(
            YandexImagesLocators.LOCATOR_YANDEX_IMAGES_FIRST_FOUND_ITEM).get_attribute('data-bem'))
        image_title = data['serp-item']['snippet']['title'].strip().replace("&quot;", '"')
        image.click()
        image_page_theme = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGES_PAGE_THEME).text
        assert image_title == image_page_theme, f"Wrong page. Expected {image_title}, got {image_page_theme}"

    def click_next(self):
        self.first_image = self.find_element(
            YandexImagesLocators.LOCATOR_YANDEX_IMAGES_ORIGINAL_IMAGE).get_attribute('src')
        next_button = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGES_BUTTON_NEXT)
        next_button.click()
        new_image = self.find_element(
            YandexImagesLocators.LOCATOR_YANDEX_IMAGES_ORIGINAL_IMAGE).get_attribute('src')
        assert self.first_image != new_image, "Image didn't change"

    def click_prev(self):
        prev_button = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGES_BUTTON_PREV)
        prev_button.click()
        image = self.find_element(
            YandexImagesLocators.LOCATOR_YANDEX_IMAGES_ORIGINAL_IMAGE).get_attribute('src')
        assert image == self.first_image, "Images don't match"
