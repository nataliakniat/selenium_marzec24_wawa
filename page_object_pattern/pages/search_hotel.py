class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
        self.search_hotel_input_xpath = "//*[@id='select2-drop']/div/input"
        self.search_hotel_match_xpath = "//span[text()='Dubai']"
        self.checkin_input_name = "checkin"
        self.checkout_input_name = "checkout"
        self.travellers_input_id = "travellersInput"
        self.adult_input_id = "adultInput"
        self.child_input_id = "childInput"
        self.search_button_xpath = "//*[@id='hotels']/form/div[5]/button"

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