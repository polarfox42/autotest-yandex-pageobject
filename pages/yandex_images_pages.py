from pages.base_page import BasePage
from pages.locators import YandexImagesLocators


class YandexImagesPage(BasePage):

    def __init__(self, driver):
        super(YandexImagesPage, self).__init__(driver)
        self.default_url = "https://yandex.ru/images/?utm_source=main_stripe_big"

    def can_see_images_link(self):
        assert self.is_element_present(YandexImagesLocators.LOCATOR_YANDEX_IMAGES_PAGE_LINK), \
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
        # TODO: исправить нажатие
        category = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGES_FIRST_POPULAR_REQUEST_ITEM)
        category_text = category.text
        category.click()
        title = self.driver.title
        assert category_text in title, f"Wrong request text. Expected {category_text}, got {title}"

    def open_first_image(self):
        image = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGES_FIRST_FOUND_ITEM)
        image.click()
        # TODO: Проверить, что открылась
