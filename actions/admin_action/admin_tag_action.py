from navigations.home_page_navigation import HomePageNavigation


class TagPageAction(HomePageNavigation):

    def open_tag_page(self, login1, password1, name_tag, edit_name):
        self.home_page_navigation(login1, password1)
        assert self.check_add_tag(name_tag), "Couldnt add TAG"
        self.check_edit_tag(edit_name), "Couldnt edit TAG"
        assert self.check_delete_tag(), "Couldnt delete TAG"
        return True
