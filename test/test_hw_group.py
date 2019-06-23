# -*- coding: utf-8 -*-

from model.hw_group import Group


def test_hw_group(app):
    app.group.create(Group(name="Zombi", header="zombi", footer="zombi"))


def test_empty_hw_group(app):
    app.group.create(Group(name="", header="", footer=""))
