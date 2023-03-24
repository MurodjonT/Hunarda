from actions.admin_directory_action import DirectoryPageAction
from base_test import TestBase


class TestDirectoryPage(TestBase):

    def test_directory_page(self):
        self.go_to_directory_page = DirectoryPageAction(self.driver)
        assert self.go_to_directory_page.open_directory_page("admin", "1234")