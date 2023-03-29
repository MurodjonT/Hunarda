from actions.admin_action.admin_tag_action import TagPageAction
from base_test import TestBase
from config import TestDatas


class TestTagPage(TestBase):

    def test_category_page(self):
        self.go_to_tag_page = TagPageAction(self.driver)
        assert self.go_to_tag_page.open_tag_page(TestDatas.login_admin, TestDatas.password_admin)