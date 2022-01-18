from pages.base_page import BasePage
from pages.locators import YandexSearchLocators


class YandexSearchPage(BasePage):

    def enter_request(self, text):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(text)
        return search_field

    def get_links_from_first_five_search_results(self):
        search_results = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_RESULTS)[:5]
        links_from_results = [element.text for element in search_results if len(element.text) > 0]
        return links_from_results

    def can_see_search_field(self):
        assert self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD), \
            "There's no search field on the page"

    def can_see_suggest(self):
        assert self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_SUGGEST), \
            "The suggest didn't appear"

    def click_enter_on_search_field(self):
        self.click_enter_on_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)

    def can_see_search_results(self):
        assert self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_RESULTS), \
            "The search results didn't appear"

    def got_link_in_top_5(self, link):
        top_five = self.get_links_from_first_five_search_results()
        result = False
        for element in top_five:
            if link == element:
                result = True
                break
        assert result, f"There's no link to {link} in top 5"
