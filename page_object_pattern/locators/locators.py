class SearchHotelLocators:
    search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
    search_hotel_input_xpath = "//*[@id='select2-drop']/div/input"
    search_hotel_match_xpath = "//span[text()='Dubai']"
    checkin_input_name = "checkin"
    checkout_input_name = "checkout"
    travellers_input_id = "travellersInput"
    adult_input_id = "adultInput"
    child_input_id = "childInput"
    search_button_xpath = "//*[@id='hotels']/form/div[5]/button"


class SearchResultLocators:
    hotel_names_xpath = "//h4[contains(@class, 'list_title')]"
