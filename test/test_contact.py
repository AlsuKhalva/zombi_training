# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts_list = app.form.get_contacts_list()
    app.form.create(Contact(first_name="aaa", last_name="aaa", mobil="999999999", email="kaka@mail.ru", day="10",
                               month="April", year="1990", notes="1"))
    new_contacts_list = app.form.get_contacts_list()
    assert len(old_contacts_list) + 1 == len(new_contacts_list)


