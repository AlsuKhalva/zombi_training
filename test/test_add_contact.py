# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contacts):
    user = json_contacts
    old_contacts_list = app.form.get_contacts_list()
    app.form.create(user)
    assert len(old_contacts_list) + 1 == app.form.count()
    new_contacts_list = app.form.get_contacts_list()
    old_contacts_list.append(user)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
