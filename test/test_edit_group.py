from model.hw_group import Group


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="VVVVVVV"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="ZUMZUM"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_header(app):
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="Bebbb"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
