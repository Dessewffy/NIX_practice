from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class Nix:
    def __init__(self, browser: Chrome):
        self.browser = browser
        self.url = "https://nixstech.com"

    def refresh(self):
        self.browser.refresh()

    def save_screen(self, path):
        self.browser.get_screenshot_as_file(path)

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def close(self):
        self.browser.close()

    # Nix webpage navigations:
    def nav_technologies(self):
        return self.browser.find_element(By.ID, "menu-item-383")

    def nav_technologies_assert(self):
        return self.browser.find_element(By.XPATH, '//*[@id="services"]/div/div/h2/p')

    def nav_vacancies(self):
        return self.browser.find_element(By.XPATH, '//li[@id="menu-item-6126"]')

    def nav_vacancies_assertion(self):
        return self.browser.find_element(By.XPATH,
                                         '//h1[@class="learn-block__text-page-title learn-block__text-page-title--large"]/p')

    def nav_courses(self):
        return self.browser.find_element(By.XPATH, '//*[@id="menu-item-5637"]/a')

    def nav_courses_assert(self):
        return self.browser.find_element(By.XPATH, '//h1[@class="learn-block__text-page-title"]')

    def nav_resources(self):
        return self.browser.find_element(By.XPATH, '//*[@id="menu-item-2334"]/a')

    def nav_resources_assert(self):
        return self.browser.find_element(By.XPATH, '//h1[@class="text-page-title"]/p')

    def nav_events(self):
        return self.browser.find_element(By.XPATH, '//*[@id="menu-item-3057"]/a')

    def nav_events_assert(self):
        return self.browser.find_element(By.XPATH, '//h2[@class="events-banner__title text-page-title"]/p/strong')

    def nav_blog(self):
        return self.browser.find_element(By.XPATH, '//*[@id="menu-item-2429"]/a')

    def nav_blog_assert(self):
        return self.browser.find_element(By.XPATH, '//h1[@class="text-page-title"]')

    def nav_contacts(self):
        return self.browser.find_element(By.XPATH, '//*[@id="menu-item-233"]/a')

    def nav_contacts_assert(self):
        return self.browser.find_element(By.XPATH, '//h2[@class="text-page-title"]/p')

    # Search field elements on the vacancies page:

    def vacancies_search_keywords(self):
        return self.browser.find_element(By.XPATH, '//*[@id="filter-input-key-word"]')

    def vacancies_categories(self):
        return self.browser.find_element(By.XPATH, '//span[@class="current"]')

    def vacancies_categories_qa(self):
        return self.browser.find_element(By.XPATH, '//li[@data-value="Quality Assurance | QA"]')

    def vacancies_level(self):
        level = self.browser.find_elements(By.XPATH, '//span[@class="current"]')
        choosen_level = [junior for junior in level]
        return choosen_level[1]

    def vacancies_level_junior(self):
        return self.browser.find_element(By.XPATH, '//li[@data-value="Junior"]')

    def search_button(self):
        return self.browser.find_element(By.XPATH, '//button[@action="load_vacancies"]')

    def vacancies_list_assert(self):
        return self.browser.find_elements(By.XPATH, '//div[@class="post-item vacancies-post-item "]')
