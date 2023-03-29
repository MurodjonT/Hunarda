from navigations.home_page_navigation import HomePageNavigation


class StaffPageAction(HomePageNavigation):

    def open_staff_page(self, login1, password1, login2, password2 ):
        self.home_page_navigation(login1, password1)
        self.check_add_staff(login2, password2)
        return True

    def open_edit_page(self, first_name, surname, email, number):
        assert self.check_edit_staff(first_name, surname, email, number)
        assert self.check_delete_user()
        return True
