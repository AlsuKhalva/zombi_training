

def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.form.delete_first_contact()
    app.session.logout()