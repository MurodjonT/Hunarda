from navigations.home_page_navigation import HomePageNavigation


class DirectoryPageAction(HomePageNavigation):

    def open_directory_page(self, login1, password1):
        self.home_page_navigation(login1, password1)
        return True

    def open_news_page(self, name, file):
        self.check_add_news(name, file)
        return True
