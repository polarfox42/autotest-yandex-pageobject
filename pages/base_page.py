from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://yandex.ru/"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}.")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}.")

    def is_element_present(self, locator, time=10):
        """ Бесполезная хрень. Ошибка все равно выводится из find_element(s)
        TODO: выпилить и заменить на простой find_element(s) """
        try:
            self.find_element(locator, time)
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False
        return True

    def click_enter_on_element(self, locator):
        self.find_element(locator).send_keys(Keys.ENTER)

    def wait_for_new_window(self, number=2, time=10):
        return WebDriverWait(self.driver, time).until(EC.number_of_windows_to_be(number),
                                                      message="Number of tabs didn't change")
