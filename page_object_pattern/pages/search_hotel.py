from page_object_pattern.locators.locators import SearchHotelLocators

class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_hotel_span_xpath = SearchHotelLocators.search_hotel_span_xpath
        self.search_hotel_input_xpath = SearchHotelLocators.search_hotel_input_xpath
        self.search_hotel_match_xpath = SearchHotelLocators.search_hotel_match_xpath
        self.checkin_input_name = SearchHotelLocators.checkin_input_name
        self.checkout_input_name = SearchHotelLocators.checkout_input_name
        self.travellers_input_id = SearchHotelLocators.travellers_input_id
        self.adult_input_id = SearchHotelLocators.adult_input_id
        self.child_input_id = SearchHotelLocators.child_input_id
        self.search_button_xpath = SearchHotelLocators.search_button_xpath

    def set_city(self, city):
        self.driver.find_element("xpath", self.search_hotel_span_xpath).click()
        self.driver.find_element("xpath", self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element("xpath", self.search_hotel_match_xpath).click()

    def set_date_range(self, checkin, checkout):
        self.driver.find_element("name", self.checkin_input_name).send_keys(checkin)
        self.driver.find_element("name", self.checkout_input_name).send_keys(checkout)

    def set_travellers(self, adult, kids):
        self.driver.find_element("id", self.travellers_input_id).click()
        self.driver.find_element("id", self.adult_input_id).clear()
        self.driver.find_element("id", self.adult_input_id).send_keys(adult)
        self.driver.find_element("id", self.child_input_id).clear()
        self.driver.find_element("id", self.child_input_id).send_keys(kids)

    def perform_search(self):
        self.driver.find_element("xpath", self.search_button_xpath).click()
