import time
from screens.screen import Screen
from selenium.webdriver.common.by import By


class TarifPageScreen(Screen):

    def __init__(self, driver):
        super().__init__(driver)

    """Tarif page add locators"""
    tarif_btn = (By.XPATH, '//*[text() = "Tariffs"]')
    add_tarif_btn = (By.XPATH, '//*[@class="v-btn v-btn--icon v-theme--light'
                               ' text-white v-btn--density-default v-btn--size-small v-btn--variant-text bg-success mt-2 rounded float-right"]')
    input_tarif_name = (By.XPATH, '//*[@placeholder="Name"]')
    save_btn_tarif = (By.XPATH, "//*[text()=\"Save\"]")
    test_tarif_btn = (By.XPATH, '//*[text()="test_tarif"]')
    test_tarif_path = (By.XPATH, '//*[text()="test_tarif"]')
    add_tarif_detail_btn = (By.XPATH, '//*[text()="Add"]')

    input_number_of = (By.XPATH, '//*[@placeholder="Number of"]')
    period_type_dropdown = (By.XPATH, '//*[@placeholder="Period type"]/parent::div')
    in_period_type = (By.XPATH, '//div[4]/div[2]/div')
    input_price = (By.XPATH, "//*[@placeholder=\"Price\"]")
    input_description = (By.XPATH, '//*[@placeholder="Description"]')
    save_btn_tarif_detail = (By.XPATH, '//*[text() = "Save"]')

    """Tarif page add locators END"""

    def check_add_tarif(self, name_tarif):
        self.click(self.tarif_btn)
        self.click(self.add_tarif_btn)
        time.sleep(1)
        self.enter_data(self.input_tarif_name, name_tarif)
        time.sleep(1)
        self.click(self.save_btn_tarif_detail)
