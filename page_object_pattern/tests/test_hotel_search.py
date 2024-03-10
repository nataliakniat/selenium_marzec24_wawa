import pytest
from selenium import webdriver
from page_object_pattern.pages.search_hotel import SearchHotelPage
from page_object_pattern.pages.search_result import SearchResultPage

class TestHotelSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_hotel_search(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/")

        search_hotel_page = SearchHotelPage(self.driver)

        # wypełnienie formularz
        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_date_range("10/03/2024", "12/03/2024")
        search_hotel_page.set_travellers("1", "2")

        # wyszukiwanie
        search_hotel_page.perform_search()

        # wyświetlanie wyników
        result_page = SearchResultPage(self.driver)

        hotels_name = result_page.get_hotels_name()

        assert hotels_name[0] == "Jumeirah Beach Hotel"
        assert hotels_name[1] == "Oasis Beach Tower"
        assert hotels_name[2] == "Rose Rayhaan Rotana"
        assert hotels_name[3] == "Hyatt Regency Perth"
