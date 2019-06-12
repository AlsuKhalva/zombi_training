def test_delete_first_group(app):
    app.session.login()
    app.form.delete_first_contact()
    app.session.logout()
