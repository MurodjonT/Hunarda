from navigations.home_page_navigation import HomePageNavigation


class CategoryPageAction(HomePageNavigation):

    def open_directory_page(self, login1, password1):
        self.home_page_navigation(login1, password1)
        return True

    def open_add_category_action(self, name_category, image_category, edit_name, edit_image):
        assert self.check_add_category(name_category, image_category)
        assert self.check_edit_category(edit_name, edit_image)
        assert self.check_delete_category()
        return True
