def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.form.edit_first_contact()
    app.session.logout()
