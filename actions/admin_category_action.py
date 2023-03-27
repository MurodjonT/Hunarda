from navigations.home_page_navigation import HomePageNavigation


class CategoryPageAction(HomePageNavigation):

    def open_directory_page(self, login1, password1):
        self.home_page_navigation(login1, password1)
        return True
