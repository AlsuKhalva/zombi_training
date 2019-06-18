from model.hw_group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="No", header="No", footer="No"))
    app.session.logout()
