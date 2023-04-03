import time

from navigations.home_page_navigation import HomePageNavigation


class HomePageAction(HomePageNavigation):

    def open_home_page(self, file, name, edit_name, edit_file):
        self.home_page_navigation("abdusamad", "teacheralex")
        assert self.check_add_course(file, name)
        assert self.check_edit_course(edit_name, edit_file)
        self.check_search_course("Test")
        time.sleep(3)
        assert self.check_delete_course()
        return True
