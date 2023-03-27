from screens.home_page_screen import HomePageScreen
from screens.admin_staffs_screen import StaffPageScreen
from screens.admin_news_screen import NewsPageScreen
from screens.admin_category_screen import CategoryPageScreen


class HomePageNavigation(HomePageScreen, StaffPageScreen,
                         NewsPageScreen, CategoryPageScreen):

    def home_page_navigation(self, login, password):
        assert self.check_open_home_page(login, password)
