# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts_list = app.form.get_contacts_list()
    user = Contact(first_name="aaa", last_name="aaa", email="kaka@mail.ru", email2="byby@bb.ru", email3="mmm@ya.ru",
                   day="10", month="April", year="1990", notes="1",
                   homephone="12399", mobilephone="12345", workphone="123456", secondaryphone="212121",
                   address="Moscow", address2="Paris")
    app.form.create(user)
    assert len(old_contacts_list) + 1 == app.form.count()
    new_contacts_list = app.form.get_contacts_list()
    old_contacts_list.append(user)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
