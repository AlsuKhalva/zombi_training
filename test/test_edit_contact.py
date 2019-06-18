from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.form.edit_first_contact(Contact(first_name="Kroha",last_name="Kartoha", mobil="777777777", email="kaka@mail.ru", day="22",
                               month="April", year="2001", notes="NoComment"))
    app.session.logout()
