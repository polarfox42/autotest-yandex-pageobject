from selenium.webdriver.common.by import By


class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_SUGGEST = (By.CSS_SELECTOR, ".mini-suggest__popup")
    LOCATOR_YANDEX_SEARCH_RESULTS = (By.CSS_SELECTOR, ".serp-item.desktop-card div.Path>a")


class YandexImagesLocators:
    LOCATOR_YANDEX_IMAGES_PAGE_LINK = (By.CSS_SELECTOR, '[data-id="images"]')
    LOCATOR_YANDEX_IMAGES_FIRST_POPULAR_REQUEST_ITEM = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0>.Link")
    LOCATOR_YANDEX_IMAGES_SEARCH_FIELD = (By.NAME, "text")
    LOCATOR_YANDEX_IMAGES_FIRST_FOUND_ITEM = (By.CLASS_NAME, "serp-item_pos_0")
    LOCATOR_YANDEX_IMAGES_ORIGINAL_IMAGE = (By.CLASS_NAME, "MMImage-Origin")
    LOCATOR_YANDEX_IMAGES_BUTTON_NEXT = (By.CLASS_NAME, "MediaViewer-ButtonNext")
    LOCATOR_YANDEX_IMAGES_BUTTON_PREV = (By.CLASS_NAME, "MediaViewer-ButtonPrev")
