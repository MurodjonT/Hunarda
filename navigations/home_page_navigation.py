from screens.home_page_screen import HomePageScreen


class HomePageNavigation(HomePageScreen):

    def home_page_navigation(self):
        assert self.check_open_home_page("abdusamad", "teacheralex")
