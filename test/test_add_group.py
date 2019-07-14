# -*- coding: utf-8 -*-

from model.hw_group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("Zombi", 10), header=random_string("zombi", 20), footer=random_string("zombi", 20))
    for i in range(5)
    ]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_hw_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_empty_hw_group(app):
 #   old_groups = app.group.get_group_list()
  #  group = Group(name="", header="", footer="")
   # app.group.create(group)
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) + 1 == len(new_groups)
    #old_groups.append(group)
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)