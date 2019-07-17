# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.add_contact import constant as testdata


@pytest.mark.parametrize("user", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, user):
    old_contacts_list = app.form.get_contacts_list()
    app.form.create(user)
    assert len(old_contacts_list) + 1 == app.form.count()
    new_contacts_list = app.form.get_contacts_list()
    old_contacts_list.append(user)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
