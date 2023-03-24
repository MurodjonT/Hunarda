from screens.home_page_screen import HomePageScreen
from screens.admin_staffs_screen import StaffPageScreen
from screens.admin_directory_screen import DirectoryPageScreen


class HomePageNavigation(HomePageScreen, StaffPageScreen, DirectoryPageScreen):

    def home_page_navigation(self, login, password):
        assert self.check_open_home_page(login, password)
