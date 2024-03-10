class SearchResultPage:

    def __init__(self, driver):
        self.driver = driver
        self.hotel_names_xpath = "//h4[contains(@class, 'list_title')]"
        # TO DO: dodac atrybut do wyswietlenia cen

    def get_hotels_name(self):
        hotels = self.driver.find_elements("xpath", self.hotel_names_xpath)
        hotels_name = [hotel.get_attribute("textContent") for hotel in hotels]
        return hotels_name

    # TO DO: metoda do pobierania cen