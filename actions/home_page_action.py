from navigations.home_page_navigation import HomePageNavigation


class HomePageAction(HomePageNavigation):

    def open_home_page(self):
        self.home_page_navigation()
        self.check_add_course()
        return True
