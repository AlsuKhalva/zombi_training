# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts_list = app.form.get_contacts_list()
    user = Contact(first_name="aaa", last_name="aaa", mobil="999999999", email="kaka@mail.ru", day="10",
                               month="April", year="1990", notes="1")
    app.form.create(user)
    new_contacts_list = app.form.get_contacts_list()
    assert len(old_contacts_list) + 1 == len(new_contacts_list)
    old_contacts_list.append(user)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
