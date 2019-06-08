# -*- coding: utf-8 -*-
import pytest
from model.hw_group import Group
from fixture.hw_application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_homework(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Zombi", header="zombi", footer="zombi"))
    app.session.logout()


def test_empty_homework(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
