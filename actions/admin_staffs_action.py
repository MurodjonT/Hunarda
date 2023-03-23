from navigations.home_page_navigation import HomePageNavigation


class StaffPageAction(HomePageNavigation):

    def open_staff_page(self, name, password):
        self.home_page_navigation()
        assert self.check_add_staff(name, password)
        return True

    def open_edit_page(self, first_name, surname, email, number):
        self.check_edit_staff(first_name, surname, email, number)
        return True