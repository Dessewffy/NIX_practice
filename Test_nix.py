import time

import settings as config
from POM import Nix



class TestNix:

    def setup_method(self):
        self.page = Nix(config.get_preconfigured_chrome_driver())
        self.page.open()
        assert self.page.browser.title == "NIX - Custom Software Development Company for IT Outsourcing"

    def teardown_method(self):
        # self.page.close()
        pass

    # Test the navigation

    def test_navigation(self):
        self.page.nav_technologies().click()
        assert self.page.nav_technologies_assert().text == "Technologies"

        self.page.nav_vacancies().click()
        assert self.page.nav_vacancies_assertion().text == "Become a part of the NIX team"

        self.page.nav_courses().click()
        assert self.page.nav_courses_assert().text == "Start your IT career journey with Free IT Courses at NIX"

        self.page.nav_resources().click()
        assert self.page.nav_resources_assert().text == "RESOURCE\nLEARNING"

        self.page.nav_events().click()
        assert self.page.nav_events_assert().text == "NIX EVENTS"

        self.page.nav_blog().click()
        assert self.page.nav_blog_assert().text == "LIFE AT NIX"

        self.page.nav_contacts().click()
        assert self.page.nav_contacts_assert().text == "OUR CONTACTS"

    # Test the search fields on the vacancies page:

    def test_vacancies_search_fields_valid(self):
        self.page.nav_vacancies().click()
        assert self.page.nav_vacancies_assertion().text == "Become a part of the NIX team"

        self.page.vacancies_search_keywords().send_keys("Junior Automation QA Engineer")
        self.page.vacancies_categories().click()
        self.page.vacancies_categories_qa().click()
        self.page.vacancies_level().click()
        self.page.vacancies_level_junior().click()
        self.page.search_button().click()

        # assertion of the listed QA vacancies:

        time.sleep(2)
        assert len(self.page.vacancies_list_assert()) == 2

