from navigations.home_page_navigation import HomePageNavigation


class TagPageAction(HomePageNavigation):

    def open_tag_page(self, login1, password1):
        self.home_page_navigation(login1, password1)
        return True
