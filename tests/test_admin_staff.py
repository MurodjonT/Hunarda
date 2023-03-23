from actions.admin_staffs_action import StaffPageAction
from base_test import TestBase


class TestHomePage(TestBase):

    def test_home_page(self):
        self.go_to_staff_page = StaffPageAction(self.driver)
        assert self.go_to_staff_page.open_staff_page("Mirtesha", "12345")
        assert self.go_to_staff_page.open_edit_page("Test", "Testov", "test@mail.com", "998909909900")