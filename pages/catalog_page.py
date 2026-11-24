from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CatalogPage:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def add_book(self, title, isbn, author, copies):
        self.driver.find_element(By.ID, "title-input").clear()
        self.driver.find_element(By.ID, "title-input").send_keys(title)
        self.driver.find_element(By.ID, "isbn-input").clear()
        self.driver.find_element(By.ID, "isbn-input").send_keys(isbn)
        self.driver.find_element(By.ID, "author-input").clear()
        self.driver.find_element(By.ID, "author-input").send_keys(author)
        self.driver.find_element(By.ID, "copies-input").clear()
        self.driver.find_element(By.ID, "copies-input").send_keys(str(copies))
        self.driver.find_element(By.ID, "add-btn").click()

    def book_row_text(self, isbn):
        row = self.wait.until(EC.presence_of_element_located((By.ID, f"row-{isbn}")))
        return row.text

    def get_available_copies_display(self, isbn):
        row = self.wait.until(EC.presence_of_element_located((By.ID, f"row-{isbn}")))
        return int(row.find_element(By.CSS_SELECTOR, ".copies").text.strip())

    def click_borrow(self, isbn):
        row = self.wait.until(EC.presence_of_element_located((By.ID, f"row-{isbn}")))
        row.find_element(By.CSS_SELECTOR, ".borrow-btn").click()

    def status_message(self):
        el = self.wait.until(EC.presence_of_element_located((By.ID, "status-msg")))
        return el.text.strip()