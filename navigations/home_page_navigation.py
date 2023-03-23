from screens.home_page_screen import HomePageScreen
from screens.admin_staffs_screen import StaffPageScreen

class HomePageNavigation(HomePageScreen, StaffPageScreen):

    def home_page_navigation(self):
        assert self.check_open_home_page("admin", "1234")
