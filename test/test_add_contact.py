# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    user = json_contacts
    old_contacts_list = db.get_contacts_list()
    app.form.create(user)
    new_contacts_list = db.get_contacts_list()
    old_contacts_list.append(user)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
    if check_ui:
        def clean(user):
            return Contact(id=user.id, first_name=user.first_name.rstrip())
        assert sorted(list(map(clean, new_contacts_list)), key=Contact.id_or_max) == sorted(app.form.get_contacts_list(),
            key=Contact.id_or_max)
