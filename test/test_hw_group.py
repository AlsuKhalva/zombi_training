# -*- coding: utf-8 -*-
from model.hw_group import Group


def test_hw_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Zombi", header="zombi", footer="zombi"))
    app.session.logout()


def test_empty_hw_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
