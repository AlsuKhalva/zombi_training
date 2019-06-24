class FormHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            "(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        self.add_new_contact()
        self.fill_contact_form(contact)
        self.return_to_home_page()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        # edit contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # submit update
        wd.find_element_by_name("update").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("mobile", contact.mobil)
        self.change_field_value("email", contact.email)
        self.change_field_value("bday", contact.day)
        self.change_field_value("bmonth", contact.month)
        self.change_field_value("byear", contact.year)
        self.change_field_value("notes", contact.notes)

    def select_month(self):
        wd = self.app.wd
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_xpath("//option[@value='April']").click()

    def select_day(self):
        wd = self.app.wd
        wd.find_element_by_name("bday").click()
        wd.find_element_by_xpath("//option[@value='4']").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if field_name == "bday":
                self.select_day()

            elif field_name == "bmonth":
                self.select_month()

            else:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))
