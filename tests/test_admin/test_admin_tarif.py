from actions.admin_action.admin_tarif_action import TarifPageAction
from base_test import TestBase
from config import TestDatas


class TestTarifPage(TestBase):

    def test_tarif_page(self):
        self.go_to_tarif_page = TarifPageAction(self.driver)
        assert self.go_to_tarif_page.open_directory_page(TestDatas.login_admin, TestDatas.password_admin, "test_tarif")
        # assert self.go_to_tarif_page.open_tarif_page_action("test_tarif")