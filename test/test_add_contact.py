# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", last_name="", email="", email2="", email3="",
                   day="", month="", year="", notes="",
                   homephone="", mobilephone="", workphone="", secondaryphone="",
                   address="", address2="")] + [
    Contact(first_name=random_string("aaa", 10), last_name=random_string("aaa", 10),
            email=random_string("kaka@mail.ru", 10), email2=random_string("byby@bb.ru", 10),
            email3=random_string("mmm@ya.ru", 10), day=random_string("10", 10),
            month=random_string("April", 10), year=random_string("1990", 10), notes=random_string("1", 10),
            homephone=random_string("12399", 10), mobilephone=random_string("12345", 10),
            workphone=random_string("123456", 10), secondaryphone=random_string("212121", 10),
            address=random_string("Moscow", 10), address2=random_string("Paris", 10))
    for i in range(3)
    ]


@pytest.mark.parametrize("user", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, user):
    old_contacts_list = app.form.get_contacts_list()
    app.form.create(user)
    assert len(old_contacts_list) + 1 == app.form.count()
    new_contacts_list = app.form.get_contacts_list()
    old_contacts_list.append(user)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
