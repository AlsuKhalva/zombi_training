from model.hw_group import Group


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="VVVVVVV"))
    app.group.edit_first_group(Group(name="ZUMZUM"))


def test_edit_first_group_header(app):
    app.group.edit_first_group(Group(header="Bebbb"))
