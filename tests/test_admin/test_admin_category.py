from actions.admin_action.admin_category_action import CategoryPageAction
from base_test import TestBase
from config import TestDatas


class TestCategoryPage(TestBase):

    def test_category_page(self):
        self.go_to_category_page = CategoryPageAction(self.driver)
        assert self.go_to_category_page.open_directory_page(TestDatas.login_admin, TestDatas.password_admin)
        assert self.go_to_category_page.open_add_category_action("test_category", "C:/zk/profskills/data/123456.jpg",
                                                                 "_edit", "C:/zk/profskills/data/123.png")