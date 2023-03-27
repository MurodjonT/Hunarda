from actions.admin_category_action import CategoryPageAction
from base_test import TestBase
from config import TestDatas


class TestCategoryPage(TestBase):

    def test_category_page(self):
        self.go_to_category_page = CategoryPageAction(self.driver)
        assert self.go_to_category_page.open_directory_page(TestDatas.login_admin, TestDatas.password_admin)