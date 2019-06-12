# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.contact_application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.form.create(Contact(first_name="aaa", middle_name="aaaaaaa", last_name="aaa", company="aa", company_address="hdhdh", phone="99999999", mobil="999999999", email="kaka@mail.ru", day="10",
                            month="April", year="1990", home_address="nndndnd x", home_number="1", notes="1"))
    app.session.logout()

