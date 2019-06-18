
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
        self.fill_form(contact)
        self.return_to_home_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # edit contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_form(contact)
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

    def fill_form(self, contact):
        wd = self.app.wd
        # name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        # phone/email
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobil)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # bday
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bday").send_keys(contact.day)
        wd.find_element_by_xpath(
            "//option[@value='10']").click()
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("bmonth").send_keys(contact.month)
        wd.find_element_by_xpath(
            "//option[@value='April']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.year)
        # other
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)