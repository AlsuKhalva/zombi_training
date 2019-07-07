from model.contact import Contact


class FormHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.add_new_contact()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath(
            "(//input[@name='submit'])[2]").click()
        self.app.open_home_page()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()

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

    def get_contacts_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        user = []
        for element in wd.find_elements_by_css_selector("tr[name='entry']"):
            el_first_name = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            user.append(Contact(first_name=el_first_name, id=id))
        return user