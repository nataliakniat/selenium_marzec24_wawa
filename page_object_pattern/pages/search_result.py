import logging
from page_object_pattern.locators.locators import SearchResultLocators


class SearchResultPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.hotel_names_xpath = SearchResultLocators.hotel_names_xpath
        # TO DO: dodac atrybut do wyswietlenia cen

    def get_hotels_name(self):
        hotels = self.driver.find_elements("xpath", self.hotel_names_xpath)
        hotels_name = [hotel.get_attribute("textContent") for hotel in hotels]
        self.logger.info("Avialable hotels:")
        for name in hotels_name:
            self.logger.info(name)
        return hotels_name

    # TO DO: metoda do pobierania cen