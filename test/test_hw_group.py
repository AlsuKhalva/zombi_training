# -*- coding: utf-8 -*-

from model.hw_group import Group


def test_hw_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="Zombi", header="zombi", footer="zombi"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_empty_hw_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
