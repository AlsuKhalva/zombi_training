# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.form.create(Contact(first_name="aaa", last_name="aaa", mobil="999999999", email="kaka@mail.ru", day="10",
                               month="April", year="1990", notes="1"))
    app.session.logout()

