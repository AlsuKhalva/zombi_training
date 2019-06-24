from model.contact import Contact


def test_delete_first_contact(app):
    if app.form.count() == 0:
        app.form.create(Contact(first_name="VVVVVVV"))
    app.form.delete_first_contact()
