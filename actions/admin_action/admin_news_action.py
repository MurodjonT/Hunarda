from navigations.home_page_navigation import HomePageNavigation


class DirectoryPageAction(HomePageNavigation):

    def open_directory_page(self, login1, password1):
        self.home_page_navigation(login1, password1)
        return True

    def open_news_page(self, name, file, description, edit_name_news, edit_description, edit_file):
        self.check_add_news(name, file, description)
        self.check_add_course_news()
        self.check_edit_test_news(edit_name_news, edit_description, edit_file)
        assert self.check_delete_test_news()
        return True
