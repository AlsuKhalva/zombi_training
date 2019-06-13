def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.form.edit_first_contact()
    app.session.logout()
