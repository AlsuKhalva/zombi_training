# -*- coding: utf-8 -*-
import pytest
from cont_group import Group
from cont_applicaton import Applicaton


@pytest.fixture
def app(request):
    fixture = Applicaton()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_contacts(app):
    app.login()
    app.contact_form(Group(first_name="aaa", middle_name="aaaaaaa", last_name="aaa", company="aa", company_address="hdhdh", phone="99999999", mobil="999999999", email="kaka@mail.ru", day="10",
                          month="April", year="1990", home_address="nndndnd x", home_number="1", notes="1"))
    app.logout()

