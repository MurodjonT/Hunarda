from actions.admin_news_action import DirectoryPageAction
from base_test import TestBase
from config import TestDatas


class TestDirectoryPage(TestBase):

    def test_directory_page(self):
        self.go_to_directory_page = DirectoryPageAction(self.driver)
        assert self.go_to_directory_page.open_directory_page(TestDatas.login_admin, TestDatas.password_admin)
        assert self.go_to_directory_page.open_news_page("test_news", "test_description","C:/zk/profskills/123456.jpg",
                                                        "_edit", "edit_test_description",
                                                        "C:/zk/profskills/123.png")