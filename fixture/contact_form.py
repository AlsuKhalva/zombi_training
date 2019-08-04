import time
from model.contact import Contact
import re

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

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        time.sleep(1)
        self.app.open_home_page()
        self.user_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
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

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_element_by_xpath("//tr[@name='entry']/td/input[@value='%s']/../.." % id)
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("phone2", contact.secondaryphone)
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
                id = element.find_element_by_name("selected[]").get_attribute("value")
                el_last_name = cells[1].text
                el_first_name = cells[2].text
                el_address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.user_cache.append(Contact(id=id, first_name=el_first_name, last_name=el_last_name,
                                               address=el_address,
                                               all_phones_from_home_page=all_phones,
                                               all_emails_from_home_page=all_emails))
        return list(self.user_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_edit_contact_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(first_name=first_name, last_name=last_name, id=id,
                       homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone,
                       email=email, email2=email2, email3=email3,
                       address=address)

    def open_user_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_user_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)
