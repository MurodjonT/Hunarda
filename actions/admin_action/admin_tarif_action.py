from navigations.home_page_navigation import HomePageNavigation


class TarifPageAction(HomePageNavigation):

    def open_directory_page(self, login1, password1, name_tarif):
        self.home_page_navigation(login1, password1)
        self.check_add_tarif(name_tarif)
        return True


