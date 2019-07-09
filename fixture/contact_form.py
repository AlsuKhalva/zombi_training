import time
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
        self.user_cache = None

    def edit_first_contact(self):
        self.select_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_edit_contact_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.user_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        time.sleep(1)
        self.app.open_home_page()
        self.user_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def select_edit_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector("img[alt='Edit']")[index].click()

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
        self.app.open_home_page()
        return len(wd.find_elements_by_css_selector("tr[name='entry']"))

    user_cache = None

    def get_contacts_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.user_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                el_first_name = cells[2].text
                el_last_name = cells[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.user_cache.append(Contact(id=id, first_name=el_first_name, last_name=el_last_name))
        return list(self.user_cache)